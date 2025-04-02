import sys
import os

# Adiciona o diretório raiz ao caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Cria um cliente de teste para simular requisições HTTP
import pytest
from fastapi.testclient import TestClient
from src.server import app

@pytest.fixture
def client():
    return TestClient(app)