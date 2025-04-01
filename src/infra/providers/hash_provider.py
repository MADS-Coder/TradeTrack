from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])


# Função usada para criptografar uma senha.
def gerar_hash(texto):
    return pwd_context.hash(texto)

# Função usada para verificar se uma senha fornecida corresponde à criptografada.
def verificar_hash(texto, hash):
    return pwd_context.verify(texto, hash)