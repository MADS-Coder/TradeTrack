def test_cadastrar_produto_sucesso(client):
    """Testa o cadastro de um novo produto com sucesso."""
    novo_produto = {
        "codigo_do_produto": 555,
        "nome_do_produto": "Celular",
        "preco_do_produto": 1000,
        "quantidade_do_produto": 4,
        "detalhes_do_produto": "Preto azulado",
        "produto_disponivel": True
    }

    response = client.post("/produto", json=novo_produto)

    assert response.status_code == 201
    # assert response.json()["codigo_do_produto"] == 555
    print("Produto cadastrado com sucesso!")


def test_cadastrar_produto_codigo_repetido(client):
    """Testa erro ao tentar cadastrar um produto com código já existente."""
    produto_repetido = {
        "codigo_do_produto": 555,  # Mesmo código do produto anterior
        "nome_do_produto": "Notebook",
        "preco_do_produto": 3000,
        "quantidade_do_produto": 2,
        "detalhes_do_produto": "Intel i7, SSD 512GB",
        "produto_disponivel": True
    }

    response = client.post("/produto", json=produto_repetido)

    assert response.status_code == 400  # Espera um erro de requisição
    # assert response.json()["detail"] == "Código do produto já cadastrado"
    print("Erro esperado: Produto com código já cadastrado!")


def test_listar_produtos(client):
    response = client.get("/produtos")
    assert response.status_code == 200
    produtos = response.json()  # Captura a resposta JSON da API
    assert isinstance(produtos, list)  # Garante que é uma lista

    # Exibe os produtos no console
    print("Lista de produtos recebida:", produtos)


def test_atualizar_produto(client):
    # Código do produto a ser atualizado.
    id_produto = 2

    dados_atualizados = {
        "codigo_do_produto": 999,
        "nome_do_produto": "TV 42 POLEGADAS",
        "preco_do_produto": 2500,
        "quantidade_do_produto": 32,
        "detalhes_do_produto": "De LED Imagem surreal",
        "produto_disponivel": True
    }

    response = client.put(f"/produto/{id_produto}", json=dados_atualizados)

    # 200 indica que a atualização foi bem-sucedida
    assert response.status_code == 200

    produto_atualizado = response.json()
   #  assert produto_atualizado["nome_do_produto"] == "Livro"

    print(f"Produto atualizado: {produto_atualizado}")


def test_atualizar_produto_inexistente(client):
    """Testa erro ao tentar atualizar um produto que não existe."""
    id_produto = 5  # Código que não existe no banco

    dados_atualizados = {
        "codigo_do_produto": 999,
        "nome_do_produto": "Tablet",
        "preco_do_produto": 1500.00,
        "quantidade_do_produto": 5,
        "detalhes_do_produto": "Tela 10 polegadas, 64GB",
        "produto_disponivel": True
    }

    response = client.put(f"/produto/{id_produto}", json=dados_atualizados)

    assert response.status_code == 404  # Espera um erro de "Não encontrado"
    # assert response.json()["detail"] == "Produto não encontrado"
    print("Erro esperado: Produto não encontrado!")


def test_deletar_produto(client):
    id_produto = 1  # Código do produto que será deletado.

    response = client.delete(f"/produto/{id_produto}")
    assert response.status_code == 200

    print(f"Produto com ID {id_produto} deletado com sucesso!")
