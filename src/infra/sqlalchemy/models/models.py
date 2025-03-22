from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
from src.infra.sqlalchemy.config.database import Base

class Venda(Base):
    
    __tablename__="vendas"

    id= Column(Integer, primary_key=True, index=True)
    código_do_produto = Column(Integer)
    nome_do_produto = Column(String)
    preço_do_produto = Column(Float)
    quantidade_do_produto = Column(Integer)
    tipo_de_pagamento = Column(String) 
    nome_do_cliente = Column(String)
