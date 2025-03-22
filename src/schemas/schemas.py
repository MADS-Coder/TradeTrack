from pydantic import BaseModel
from typing import Optional


class Venda(BaseModel):

    id: Optional[int]
    código_do_produto: int
    nome_do_produto: str
    preço_do_produto: float
    quantidade_do_produto: int
    tipo_de_pagamento: str
    nome_do_cliente: str

    class Config:
        orm_mode = True
