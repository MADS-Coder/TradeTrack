from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.schemas.schemas import LoginData, VendedorSimples, Vendedor
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositoriovendedor import RepositorioVendedor
from src.routers.auth_utils import obter_usuario_logado
from src.infra.providers import hash_provider, token_provider

router = APIRouter()


@router.post('/token')
def login(login_data: LoginData, db: Session = Depends(get_db)):
    senha = login_data.senha
    matricula = login_data.matricula

    # Verifica se o vendedor existe no banco de dados
    vendedor = RepositorioVendedor(db).obter_matricula_vendedor(matricula)

    if not vendedor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Matrícula ou senha incorretas."
        )

    # Verifica se a senha fornecida corresponde ao hash armazenado
    senha_valida = hash_provider.verificar_hash(senha, vendedor.senha)

    if not senha_valida:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Matrícula ou senha incorretas."
        )

    # Gera o token, incluindo a 'matricula' do vendedor.
    token = token_provider.criar_access_token({'sub': vendedor.matricula})
    return {'vendedor': vendedor, 'access_token': token}


@router.get('/me', response_model=VendedorSimples)
def me(vendedor: Vendedor = Depends(obter_usuario_logado)):
    return vendedor
