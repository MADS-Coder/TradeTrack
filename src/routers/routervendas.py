from fastapi import APIRouter, Depends
from typing import List
from src.infra.sqlalchemy.config.database import get_db
from sqlalchemy.orm import Session
from src.schemas.schemas import Venda, VendaSimples
from src.infra.sqlalchemy.repositorios.repositoriovendas import RepositorioVenda


router = APIRouter()


# Cria uma Venda para um produto.
@router.post('/venda')
def vendas_de_produtos(vendas: Venda, db: Session = Depends(get_db)):
    vender_produto = RepositorioVenda(db).vender_produtos(vendas)
    return vender_produto


# Lista todas as vendas realizadas.
@router.get('/vendas', response_model=List[VendaSimples])
def listar_venda_por_produto(db: Session = Depends(get_db)):
    listar_vendas_por_produtos = RepositorioVenda(db).listar_venda_por_produto()
    return listar_vendas_por_produtos
