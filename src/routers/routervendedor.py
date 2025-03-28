from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.infra.sqlalchemy.config.database import get_db
from sqlalchemy.orm import Session
from src.schemas.schemas import Vendedor, VendedorSimples
from src.infra.sqlalchemy.repositorios.repositoriovendedor import RepositorioVendedor


router = APIRouter()


# Cadastra vendedor
@router.post('/vendedor')
def criar_vendedor(vendedor: Vendedor, db: Session = Depends(get_db)):
    criar_vendedor = RepositorioVendedor(db).criar_vendedor(vendedor)
    return criar_vendedor


# Lista todos os vendedores cadastrados
@router.get('/vendedores', response_model=List[VendedorSimples])
def listar_vendedores(db: Session = Depends(get_db)):
    vendedores = RepositorioVendedor(db).listar_vendedor()
    return vendedores


@router.delete('/vendedor/{usuario_do_vendedor}')
def remover_vendedor(usuario_do_vendedor: str, db: Session = Depends(get_db)):
    deletar_vendedor = RepositorioVendedor(
        db).remover_vendedor(usuario_do_vendedor)
    if not deletar_vendedor:
        raise HTTPException(
            status_code=404, detail=f'{usuario_do_vendedor} não localizado!'
        )
    return deletar_vendedor
