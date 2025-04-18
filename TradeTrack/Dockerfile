# Usa a imagem oficial do Python, versão slim (mais leve)
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . /app

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Informa a porta que a aplicação vai utilizar (a mesma usada no CMD)
EXPOSE 8000

# Comando para iniciar o servidor Uvicorn (modo produção, sem --reload)
CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "8000"]


