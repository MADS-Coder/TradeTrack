from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Produtos(Base):

    __tablename__ = "produto"

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
        Integer, ForeignKey('produto.codigo_do_produto'))
    nome_do_produto = Column(String)
    preco_do_produto = Column(Float)
    quantidade_do_produto = Column(Integer)
    tipo_de_pagamento = Column(String)
    nome_do_cliente = Column(String)
    id_vendedor = Column(Integer, ForeignKey('vendedores.id'))

    # Relacionamento com Produtos (Um para Muitos)
    produto = relationship('Produtos', back_populates='vendas')

    # Relacionamento com Vendedor (Muitos para 1)
    vendedor = relationship('Vendedor', back_populates='vendas')


class Vendedor(Base):

    __tablename__ = "vendedores"

    id = Column(Integer, primary_key=True, index=True)
    usuario_do_vendedor = Column(String)
    matricula = Column(String)
    senha = Column(String)

    # Relacionamento com Vendas (Um para muitos)
    vendas = relationship('Venda', back_populates='vendedor') # Venda realizada pelo vendedor.
