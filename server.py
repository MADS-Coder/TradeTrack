from fastapi import FastAPI, Depends
from src.schemas.schemas import Venda
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, create_db
from src.infra.sqlalchemy.repositorios.repositoriovendas import RepositorioVenda

create_db()

app = FastAPI()


@app.post('/vendas')
def vendas_de_produtos(vendas: Venda, db: Session = Depends(get_db)):
    vender_produto = RepositorioVenda(db).vender_produtos(vendas)
    return vender_produto


@app.get('/vendas')
def listar_venda_por_produto():
    return {'mensagem': 'Esse campo lista as vendas realizadas.'}
