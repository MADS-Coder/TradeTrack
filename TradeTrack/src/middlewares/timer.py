# Importa a biblioteca padrão do Python para medir o tempo de execução.
import time
from fastapi import Request

async def processar_tempo_requisicao(request: Request, next):
    #print('Interceptou chegada...')
    
    start_time = time.perf_counter()  # Marca o tempo antes da requisição
    
    response = await next(request)  # Chama o próximo middleware ou rota
    
    process_time = time.perf_counter() - start_time  # Calcula o tempo de processamento
    #print('Interceptou volta...')
    
    response.headers["X-Process-Time"] = str(process_time)  # Adiciona o tempo no cabeçalho
    return response  # Retorna a resposta corretamente