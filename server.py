from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import routerprodutos, routervendas, routervendedores, routerauth

app = FastAPI()

origins = ['http://localhost:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Rotas VENDAS
app.include_router(routervendas.router)

# Rotas PRODUTOS
app.include_router(routerprodutos.router)

# Rotas VENDEDORES
app.include_router(routervendedores.router)

# Rotas SEGURANÇA: Autenticação e Autorização
app.include_router(routerauth.router, prefix="/auth")
