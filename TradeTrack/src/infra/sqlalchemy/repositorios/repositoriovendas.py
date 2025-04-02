from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import select


class RepositorioVenda:

    def __init__(self, db: Session):
        self.db = db


    def vender_produtos(self, venda: schemas.CriarVenda):
        # Verifica se o produto existe
        produto = self.db.query(models.Produtos).filter(
            models.Produtos.codigo_do_produto == venda.venda_codigo_do_produto).first()

        if not produto:
            raise HTTPException(
                status_code=404,
                detail=f'Produto com código {venda.venda_codigo_do_produto} não encontrado!')

        # Verifica se a quantidade do produto é suficiente para a venda
        if produto.quantidade_do_produto < venda.quantidade_vendida:
            raise HTTPException(
                status_code=400,
                detail=f'Não há quantidade suficiente do produto {venda.venda_codigo_do_produto}.\
                Disponível: {produto.quantidade_do_produto}, solicitada: {venda.quantidade_vendida}.'
            )

        # Verificar se o vendedor existe
        vendedor = self.db.query(models.Vendedor).filter(
            models.Vendedor.id == venda.id_vendedor).first()

        if not vendedor:
            raise HTTPException(
                status_code=403,
                detail=f'Vendedor com ID {venda.id_vendedor} não está cadastrado!')

        # Cria a venda preenchendo automaticamente os dados do produto
        db_venda = models.Venda(
            venda_codigo_do_produto=produto.codigo_do_produto,
            nome_do_produto=produto.nome_do_produto,
            preco_do_produto=produto.preco_do_produto,
            quantidade_do_produto=produto.quantidade_do_produto,
            tipo_de_pagamento=venda.tipo_de_pagamento,
            nome_do_cliente=venda.nome_do_cliente,
            id_vendedor=vendedor.id
        )

        # Atualiza a quantidade do produto no estoque
        produto.quantidade_do_produto -= venda.quantidade_vendida  # Subtrai a quantidade vendida do estoque
        self.db.commit()
        self.db.refresh(produto)

        # Registra a venda no banco
        self.db.add(db_venda)
        self.db.commit()
        self.db.refresh(db_venda)
        
        return db_venda


    def listar_venda_por_produto(self):
        # Cria uma instrução de seleção (SELECT) para buscar todas as vendas na tabela 'vendas'.
        consultar_vendas = select(models.Venda)

        # Executa a consulta no banco de dados.
        resultado = self.db.execute(consultar_vendas).scalars().all()

        # Retorna a lista de vendas encontradas
        return resultado
    

    def remover_vendas(self, id_venda):
        # Cria uma consulta no banco de dados para a tabela 'Vendas'
        venda = self.db.query(models.Venda).filter(
            models.Venda.id == id_venda).first()

        if not venda:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Codigo {venda} não encontrado!'
            )
    
        # Se o vendedor existir, remove ele do banco de dados
        self.db.delete(venda)
        # Confirma a operação de exclusão no banco de dados
        self.db.commit()

        # Retorna uma mensagem indicando sucesso na exclusão
        return {'Mensagem': f'A venda do produto de (ID {id_venda} - {venda.nome_do_produto}) foi removida com sucesso!'}
