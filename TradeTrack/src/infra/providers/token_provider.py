#Define a validade, fazendo operações com datas.
from datetime import datetime, timedelta, timezone
#Serve para gerar e verificar o JWT token.
import jwt                     


#CONFIG
SECRET_KEY = 'caa9c8f8620cbb30679026bb6427e11f'
ALGORITHM = 'HS256'
#Validade do token é 3000 minutos.
EXPIRES_IN_MIN = 3000             



# CRIA E RETORNA O TOKEN
def criar_access_token(data: dict, expiracao: timedelta | None = None):
    #Faz uma copia do dicionario (data)
    dados = data.copy()
    if expiracao:
        expire = datetime.now(timezone.utc) + expiracao
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    dados.update({"exp": expire})
    encoded_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verificar_access_token(token: str):
    try:
        carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("Token decodificado:", carga)  # Depuração
        return carga.get('sub')
    except jwt.ExpiredSignatureError:
        print("Erro: Token expirado!")
        return None
    except jwt.InvalidTokenError as e:
        print(f"Erro: Token inválido! Detalhes: {str(e)}")
        return None

