from src.infra.sqlalchemy.repositorios.repositoriovendedor import RepositorioVendedor
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from starlette import status
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider
from jwt import PyJWTError

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


def obter_usuario_logado(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido Essa merda')

    # Verifica e decodifica o token
    try:
        vendedor_matricula = token_provider.verificar_access_token(token)
    except PyJWTError:
        raise exception  # Se houver erro ao verificar o token, retorna erro de token inválido

    if not vendedor_matricula:
        raise exception  # Se não conseguir extrair o id do token, retorna erro de token inválido

    # Busca o vendedor pela matricula
    vendedor = RepositorioVendedor(db).obter_matricula_vendedor(vendedor_matricula)

    if not vendedor:
        raise exception  # Se o vendedor não for encontrado, retorna erro de não autorizado

    return vendedor
