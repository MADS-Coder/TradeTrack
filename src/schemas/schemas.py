from pydantic import BaseModel
from typing import Optional


class Produtos(BaseModel):
    id: Optional[int]
    codigo_do_produto: int
    nome_do_produto: str
    preco_do_produto: float
    quantidade_do_produto: int
    detalhes_do_produto: str
    produto_disponivel: bool

    class Config:
        orm_mode = True  # Permite converter objetos ORM para JSON


class Venda(BaseModel):

    id: Optional[int]
    venda_codigo_do_produto: int
    nome_do_produto: str
    preco_do_produto: float
    quantidade_do_produto: int
    tipo_de_pagamento: str
    nome_do_cliente: str

    class Config:
        orm_mode = True  # Permite converter objetos ORM para JSON
