from pydantic import BaseModel
from typing import Optional, List


class Vendedor(BaseModel):
    id: Optional[int] = None
    usuario_do_vendedor: str
    senha: str

    class Config:
        orm_mode = True  # Permite converter objetos ORM para JSON


class VendedorSimples(BaseModel):
    id: Optional[int] = None
    usuario_do_vendedor: str

    class Config:
        orm_mode = True  # Permite converter objetos ORM para JSON


class Venda(BaseModel):
    id: Optional[int] = None
    venda_codigo_do_produto: int
    nome_do_produto: str
    preco_do_produto: float
    quantidade_do_produto: int
    tipo_de_pagamento: str
    nome_do_cliente: str
    id_vendedor: int

    class Config:
        orm_mode = True  # Permite converter objetos ORM para JSON


class VendaSimples(BaseModel):
    id: int
    venda_codigo_do_produto: int
    nome_do_produto: str
    preco_do_produto: float
    quantidade_do_produto: int
    tipo_de_pagamento: str
    vendedor: Optional[VendedorSimples] = None  # Relacionamento com Vendedor

    class Config:
        orm_mode = True


class ProdutoSimples(BaseModel):
    id: int
    codigo_do_produto: int
    nome_do_produto: str
    preco_do_produto: float
    quantidade_do_produto: int
    detalhes_do_produto: str

    class Config:
        orm_mode = True


class Produtos(BaseModel):
    id: Optional[int] = None
    codigo_do_produto: int
    nome_do_produto: str
    preco_do_produto: float
    quantidade_do_produto: int
    detalhes_do_produto: str
    produto_disponivel: bool

    class Config:
        orm_mode = True  # Permite converter objetos ORM para JSON
