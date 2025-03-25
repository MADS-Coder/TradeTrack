from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import select


class RepositorioVenda:

    def __init__(self, db: Session):
        self.db = db

    def vender_produtos(self, venda: schemas.Venda):
        db_venda = models.Venda(venda_codigo_do_produto=venda.venda_codigo_do_produto, nome_do_produto=venda.nome_do_produto,
                                preco_do_produto=venda.preco_do_produto, quantidade_do_produto=venda.quantidade_do_produto,
                                tipo_de_pagamento=venda.tipo_de_pagamento, nome_do_cliente=venda.nome_do_cliente)

        self.db.add(db_venda)
        self.db.commit()
        self.db.refresh(db_venda)
        return db_venda

    def listar_venda_por_produto(self):
        consultar_vendas = select(models.Venda)
        resultado = self.db.execute(consultar_vendas).scalars().all()
        return resultado
