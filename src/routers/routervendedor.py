from fastapi import APIRouter, Depends
from typing import List
from src.infra.sqlalchemy.config.database import get_db
from sqlalchemy.orm import Session
from src.schemas.schemas import Vendedor, VendedorSimples
from src.infra.sqlalchemy.repositorios.repositoriovendedor import RepositorioVendedor


router = APIRouter()


# Cadastra vendedor
@router.post('/vendedor')
def criar_produto(vendedor: Vendedor, db: Session = Depends(get_db)):
    criar_vendedor = RepositorioVendedor(db).criar_vendedor(vendedor)
    return criar_vendedor


# Lista todos os vendedores cadastrados
@router.get('/vendedores', response_model=List[VendedorSimples])
def listar_produtos(db: Session = Depends(get_db)):
    vendedores = RepositorioVendedor(db).listar_vendedor()
    return vendedores