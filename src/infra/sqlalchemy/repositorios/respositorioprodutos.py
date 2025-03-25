from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import select


class RepositorioProduto:

    def __init__(self, db: Session):
        self.db = db

    def criar_produto(self, produto: schemas.Produtos):
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

    def editar_produto():
        ...

    def deletar_produto():
        ...
