def test_realizar_venda_sucesso(client):
    """Testa uma venda bem-sucedida."""
    venda = {
        "venda_codigo_do_produto": 234,
        "tipo_de_pagamento": "Cartão",
        "nome_do_cliente": "João Silva",
        "id_vendedor": 2,
        "quantidade_vendida": 1
    }
    response = client.post("/venda", json=venda)

    assert response.status_code == 201
    #assert response.json()["mensagem"] == "Venda realizada com sucesso!"
    print("Venda realizada com sucesso!")


def test_realizar_venda_produto_inexistente(client):
    """Testa erro ao vender um produto que não existe."""
    venda = {
        "venda_codigo_do_produto": 434,
        "tipo_de_pagamento": "Cartão",
        "nome_do_cliente": "João Silva",
        "id_vendedor": 2,
        "quantidade_vendida": 1
    }
    response = client.post("/venda", json=venda)

    assert response.status_code == 404
    #assert response.json()["detail"] == "Produto não encontrado"
    print("Erro esperado: Produto não encontrado")


def test_realizar_venda_estoque_insuficiente(client):
    """Testa erro ao vender mais do que o estoque disponível."""
    venda = {
        "venda_codigo_do_produto": 234,
        "tipo_de_pagamento": "Cartão",
        "nome_do_cliente": "João Silva",
        "id_vendedor": 2,
        "quantidade_vendida": 30
    }
    response = client.post("/venda", json=venda)

    assert response.status_code == 400
    #assert response.json()["detail"] == "Estoque insuficiente"
    print("Erro esperado: Estoque insuficiente")


def test_realizar_venda_vendedor_inexistente(client):
    """Testa erro ao tentar vender com um vendedor inexistente."""
    venda = {
        "venda_codigo_do_produto": 234,
        "tipo_de_pagamento": "Cartão",
        "nome_do_cliente": "João Silva",
        "id_vendedor": 9,
        "quantidade_vendida": 1
    }
    response = client.post("/venda", json=venda)

    assert response.status_code == 403
    #assert response.json()["detail"] == "Vendedor não encontrado"
    print("Erro esperado: Vendedor não encontrado")


def test_listar_vendas(client):
    """Testa a listagem de vendas."""
    response = client.get("/vendas")

    assert response.status_code == 200
    #assert isinstance(response.json(), list)  # Deve retornar uma lista
    print("Lista de vendas:", response.json())


def test_deletar_venda(client):
    """Testa a exclusão de uma venda pelo código do produto."""
    id_venda = 3  # Código de um produto já cadastrado
    response = client.delete(f"/venda/{id_venda}")

    assert response.status_code == 200
    #assert response.json()["mensagem"] == "Venda deletada com sucesso!"
    print("Venda deletada com sucesso!")
