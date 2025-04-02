from fastapi import APIRouter, Depends, status
from typing import List
from src.infra.sqlalchemy.config.database import get_db
from sqlalchemy.orm import Session
from src.schemas.schemas import Vendedor, VendedorSimples, VendedorUpdate
from src.infra.sqlalchemy.repositorios.repositoriovendedor import RepositorioVendedor


router = APIRouter()


# Cadastra vendedor
@router.post('/vendedor', status_code=status.HTTP_201_CREATED, response_model=VendedorSimples)
def criar_vendedor(vendedor: Vendedor, db: Session = Depends(get_db)):
    vendedor_criado = RepositorioVendedor(db).criar_vendedor(vendedor)
    return vendedor_criado


@router.get('/vendedores', response_model=List[VendedorSimples])
def listar_vendedores(db: Session = Depends(get_db)):
    vendedores = RepositorioVendedor(db).listar_vendedor()
    return vendedores


@router.get('/vendedores/{matricula}', response_model=VendedorSimples)
def obter_vendedor(matricula: str, db: Session = Depends(get_db)):
    vendedor = RepositorioVendedor(db).obter_matricula_vendedor(matricula)
    return vendedor


@router.put('/vendedor/{matricula_vendedor}', status_code=status.HTTP_426_UPGRADE_REQUIRED, response_model=VendedorSimples)
def atualizar_produto(matricula_vendedor: str, vendedor: VendedorUpdate, db: Session = Depends(get_db)):
    resultado = RepositorioVendedor(db).atualizar_vendedor(matricula_vendedor, vendedor)
    return resultado


@router.delete('/vendedor/{matricula_vendedor}')
def remover_vendedor(matricula_vendedor: str, db: Session = Depends(get_db)):
    deletar_vendedor = RepositorioVendedor(db).remover_vendedor(matricula_vendedor)
    return deletar_vendedor


