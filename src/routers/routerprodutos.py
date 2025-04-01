from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.infra.sqlalchemy.config.database import get_db
from sqlalchemy.orm import Session
from src.schemas.schemas import Produtos, ProdutoSimples
from src.infra.sqlalchemy.repositorios.respositorioprodutos import RepositorioProduto


router = APIRouter()


# Cadastra os produtos
@router.post('/produto', response_model=ProdutoSimples)
def criar_produto(produtos: Produtos, db: Session = Depends(get_db)):
    cadastrar_produto = RepositorioProduto(db).criar_produto(produtos)
    return cadastrar_produto


# Lista todos os produtos cadastrados
@router.get('/produtos', response_model=List[ProdutoSimples])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar_produtos()
    return produtos


# Edita o produto selecionado pelo código
@router.put('/produto/{codigo_do_produto}', response_model=Produtos)
def atualizar_produto(codigo_do_produto: int, produto: Produtos, db: Session = Depends(get_db)):
    RepositorioProduto(db).editar_produto(codigo_do_produto, produto)
    produto.codigo_do_produto = codigo_do_produto
    return produto


# Remove o produto pelo codigo_do_produto.
@router.delete('/produto/{codigo_do_produto}')
def remover_produto(codigo_do_produto: int, db: Session = Depends(get_db)):
    deletar_produto = RepositorioProduto(db).deletar_produto(codigo_do_produto)
    return deletar_produto
