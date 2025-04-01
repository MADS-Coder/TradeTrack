from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import select, delete, update


class RepositorioProduto:

    def __init__(self, db: Session):
        self.db = db

    def criar_produto(self, produto: schemas.Produtos):
        # Verifica se já existe um produto com o mesmo código no banco
        produto_existente = self.db.query(models.Produtos).filter(
            models.Produtos.codigo_do_produto == produto.codigo_do_produto).first()

        if produto_existente:
            raise HTTPException(
                status_code=400,
                detail=f'O código {produto.codigo_do_produto} já está cadastrado para outro produto!'
            )
        
        # Se não existir, cadastra o novo produto
        db_produto = models.Produtos(codigo_do_produto=produto.codigo_do_produto, nome_do_produto=produto.nome_do_produto,
                                     preco_do_produto=produto.preco_do_produto, quantidade_do_produto=produto.quantidade_do_produto,
                                     detalhes_do_produto=produto.detalhes_do_produto, produto_disponivel=produto.produto_disponivel)
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto


    def listar_produtos(self):
        listar_produtos = select(models.Produtos)  # Consulta
        # Executa a consulta e extrai os valores das colunas
        produtos = self.db.execute(listar_produtos).scalars().all()
        return produtos


    def editar_produto(self, id: int, produto: schemas.Produtos):
        # UPDATE - Cria uma instrução de atualização para a tabela 'Produtos'
        # WHERE - Define a condição para atualizar apenas o produto com o ID correspondente.
        # VALUES - Define os novos valores que serão atribuídos às colunas do produto
        update_produto = update(models.Produtos).where(
            models.Produtos.id == id).values(codigo_do_produto=produto.codigo_do_produto,
                                             nome_do_produto=produto.nome_do_produto, preco_do_produto=produto.preco_do_produto,
                                             quantidade_do_produto=produto.quantidade_do_produto, detalhes_do_produto=produto.detalhes_do_produto,
                                             produto_disponivel=produto.produto_disponivel)
        # Executa a instrução de atualização no banco de dados
        self.db.execute(update_produto)

        # Confirma a transação para salvar as alterações no banco de dados
        self.db.commit()


    def deletar_produto(self, codigo_do_produto):
        # Cria uma consulta no banco de dados para a tabela 'Produtos'
        produto = self.db.query(models.Produtos).filter(
            models.Produtos.codigo_do_produto == codigo_do_produto).first()

        if not produto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'{codigo_do_produto} do produto não localizado!.'
            )
    
        # Se o produto existir, remove ele do banco de dados
        self.db.delete(produto)
        # Confirma a operação de exclusão no banco de dados
        self.db.commit()

        # Acessa o nome do produto deletado
        return {'Mensagem': f'Produto {produto.nome_do_produto} removido com sucesso!'}