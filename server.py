from fastapi import FastAPI, Depends
from src.schemas.schemas import Venda, Produtos
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, create_db
from src.infra.sqlalchemy.repositorios.repositoriovendas import RepositorioVenda
from src.infra.sqlalchemy.repositorios.respositorioprodutos import RepositorioProduto

create_db()

app = FastAPI()


@app.post('/vendas')
def vendas_de_produtos(vendas: Venda, db: Session = Depends(get_db)):
    vender_produto = RepositorioVenda(db).vender_produtos(vendas)
    return vender_produto


@app.get('/vendas')
def listar_venda_por_produto():
    return {'mensagem': 'Esse campo lista as vendas realizadas.'}


@app.post('/produto')
def criar_produto(produtos: Produtos, db: Session = Depends(get_db)):
    cadastrar_produto = RepositorioProduto(db).criar_produto(produtos)
    return cadastrar_produto


@app.get('/produtos')
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar_produtos()
    return produtos
