from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Produtos(Base):

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    codigo_do_produto = Column(Integer, unique=True, index=True)
    nome_do_produto = Column(String)
    preco_do_produto = Column(Float)
    quantidade_do_produto = Column(Integer)
    detalhes_do_produto = Column(String)
    produto_disponivel = Column(Boolean)

    # Relacionamento com Vendas (Muitos para um)
    vendas = relationship('Venda', back_populates='produto')


class Venda(Base):

    __tablename__ = "vendas"

    id = Column(Integer, primary_key=True, index=True)
    venda_codigo_do_produto = Column(
        Integer, ForeignKey('produtos.codigo_do_produto'))
    nome_do_produto = Column(String)
    preco_do_produto = Column(Float)
    quantidade_do_produto = Column(Integer)
    tipo_de_pagamento = Column(String)
    nome_do_cliente = Column(String)

    # Relacionamento com Produtos (Um para Muitos)
    produto = relationship('Produtos', back_populates='vendas')
