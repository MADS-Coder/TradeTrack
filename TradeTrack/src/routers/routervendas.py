from fastapi import APIRouter, Depends, status
from typing import List
from src.infra.sqlalchemy.config.database import get_db
from sqlalchemy.orm import Session
from src.schemas.schemas import CriarVenda, VendaSimples
from src.infra.sqlalchemy.repositorios.repositoriovendas import RepositorioVenda


router = APIRouter()


# Cria uma Venda para um produto.
@router.post('/venda', status_code=status.HTTP_201_CREATED)
def vendas_de_produtos(vendas: CriarVenda, db: Session = Depends(get_db)):
    vender_produto = RepositorioVenda(db).vender_produtos(vendas)
    return vender_produto


# Lista todas as vendas realizadas.
@router.get('/vendas', response_model=List[VendaSimples])
def listar_venda_por_produto(db: Session = Depends(get_db)):
    listar_vendas_por_produtos = RepositorioVenda(db).listar_venda_por_produto()
    return listar_vendas_por_produtos


@router.delete('/venda/{id_venda}')
def remover_uma_venda(id_venda: int, db: Session = Depends(get_db)):
    deletar_uma_venda = RepositorioVenda(db).remover_vendas(id_venda)
    return deletar_uma_venda
