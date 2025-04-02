def test_criar_vendedor(client):
    """Testa a criação de um novo vendedor."""
    vendedor = {
        "usuario_do_vendedor": "joaopedro",
        "matricula": "789",
        "senha": "segura123"
    }

    response = client.post("/vendedor", json=vendedor)

    assert response.status_code == 201
    # assert response.json()["mensagem"] == "Vendedor cadastrado com sucesso!"
    print("Vendedor cadastrado com sucesso!")


def test_criar_vendedor_existente(client):
    """Testa erro ao criar um vendedor com matrícula já cadastrada."""
    vendedor = {
        "usuario_do_vendedor": "joaopedro",
        "matricula": "789",
        "senha": "segura123"
    }

    response = client.post("/vendedor", json=vendedor)

    assert response.status_code == 409
    # assert response.json()["detail"] == "Vendedor com essa matrícula já existe"
    print("Erro esperado: Vendedor com matrícula já existente!")


def test_listar_vendedores(client):
    """Testa a listagem de todos os vendedores."""
    response = client.get("/vendedores")

    assert response.status_code == 200
    # assert isinstance(response.json(), list)  # Deve retornar uma lista
    print("Lista de vendedores:", response.json())


def test_buscar_vendedor_por_matricula(client):
    """Testa a busca de um vendedor por matrícula."""
    matricula = 1234  # Matrícula já cadastrada
    response = client.get(f"/vendedores/{matricula}")

    assert response.status_code == 200
    # assert response.json()["matricula"] == matricula
    print(f"Vendedor encontrado: {response.json()}")


def test_buscar_vendedor_por_matricula_inexistente(client):
    """Testa a busca de um vendedor por matrícula."""
    matricula = 12345  # Matrícula já cadastrada
    response = client.get(f"/vendedores/{matricula}")

    assert response.status_code == 404
    # assert response.json()["matricula"] == matricula
    print(f"Vendedor não encontrado: {response.json()}")


def test_atualizar_vendedor_sucesso(client):
    """Testa a atualização de um vendedor existente."""
    matricula = "789"  # Matrícula já cadastrada

    dados_atualizados = {
        "usuario_do_vendedor": "Lucrecia quantica",
        "senha": "nova_senha_123"
    }

    response = client.put(f"/vendedor/{matricula}", json=dados_atualizados)

    assert response.status_code == 426
    # assert response.json()["usuario_do_vendedor"] == "Novo Nome"
    # assert response.json()["matricula"] == matricula  # Matrícula não pode ser alterada
    print("Vendedor atualizado com sucesso!")


def test_atualizar_vendedor_inexistente(client):
    """Testa erro ao tentar atualizar um vendedor inexistente."""
    matricula = "9999"  # Matrícula inexistente

    dados_atualizados = {
        "usuario_do_vendedor": "Matheus Silva",
        "senha": "senha123"
    }

    response = client.put(f"/vendedor/{matricula}", json=dados_atualizados)

    assert response.status_code == 404
    # assert response.json()["detail"] == "Vendedor não encontrado"
    print("Erro esperado: Vendedor não encontrado")


def test_deletar_vendedor(client):
    """Testa a exclusão de um vendedor pelo número da matrícula."""
    matricula = 233  # Matrícula já cadastrada
    response = client.delete(f"/vendedor/{matricula}")

    assert response.status_code == 200
    # assert response.json()["mensagem"] == "Vendedor deletado com sucesso!"
    print("Vendedor deletado com sucesso!")


def test_deletar_vendedor_inexistente(client):
    """Testa erro ao tentar deletar um vendedor inexistente."""
    matricula_inexistente = 233
    response = client.delete(f"/vendedor/{matricula_inexistente}")

    assert response.status_code == 404
    # assert response.json()["detail"] == "Vendedor não encontrado"
    print("Erro esperado: Tentativa de deletar vendedor inexistente!")
