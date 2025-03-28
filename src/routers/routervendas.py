from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.infra.sqlalchemy.config.database import get_db
from sqlalchemy.orm import Session
from src.schemas.schemas import CriarVenda, VendaSimples
from src.infra.sqlalchemy.repositorios.repositoriovendas import RepositorioVenda


router = APIRouter()


# Cria uma Venda para um produto.
@router.post('/venda')
def vendas_de_produtos(vendas: CriarVenda, db: Session = Depends(get_db)):
    vender_produto = RepositorioVenda(db).vender_produtos(vendas)
    return vender_produto


# Lista todas as vendas realizadas.
@router.get('/vendas', response_model=List[VendaSimples])
def listar_venda_por_produto(db: Session = Depends(get_db)):
    listar_vendas_por_produtos = RepositorioVenda(
        db).listar_venda_por_produto()
    return listar_vendas_por_produtos


@router.delete('/venda/{venda_codigo_do_produto}')
def remover_uma_venda(venda_codigo_do_produto: int, db: Session = Depends(get_db)):
    deletar_uma_venda = RepositorioVenda(
        db).remover_vendas(venda_codigo_do_produto)
    if not deletar_uma_venda:
        raise HTTPException(
            status_code=404, detail=f'O código {venda_codigo_do_produto} não foi localizado!'
        )
    return deletar_uma_venda
