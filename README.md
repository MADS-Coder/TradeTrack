# TradeTrack – Rastreamento de Vendas e Estoque

### 📍 **Sobre o projeto**

**TradeTrack** é uma aplicação backend desenvolvida com FastAPI e SQLAlchemy para o gerenciamento de vendas e controle de estoque. O sistema permite o cadastro, edição, remoção e listagem de produtos, bem como o registro e consulta de vendas.

O projeto foi desenvolvido para demonstrar habilidades em desenvolvimento backend, incluindo boas práticas como separação de responsabilidades, uso de ORM, criação de testes e implementação de autenticação JWT.

Além disso, foi criado um arquivo `requirements.txt` para facilitar a instalação das dependências do projeto, bem como um `Dockerfile` para possibilitar a criação de containers da aplicação. O deploy foi realizado na plataforma **Render**, com autenticação via GitHub, permitindo integração contínua e facilidade na atualização da API.

**Segue o link:** `https://tradetrack-gg9g.onrender.com/docs`

⚙️ **Tecnologias Utilizadas**

- **Python**: Linguagem principal do projeto.
- **FastAPI**: Framework moderno e assíncrono para criação de APIs.
- **SQLAlchemy**: ORM para interagir com o banco de dados de forma eficiente.
- **SQLite**: Banco de dados leve utilizado para armazenamento.
- **Alembic**: Ferramenta de migração para gerenciamento da estrutura do banco.
- **Pytest**: Framework para testes unitários e de integração.
- **JWT (Json Web Token)**: Implementado para autenticação e segurança dos endpoints.
- **Insomnia**: Utilizado para testar as requisições da API.
- **VS Code**: Editor de código utilizado no desenvolvimento.

## **Funcionalidades Implementadas**

- **Cadastro de Produtos** – Registra produtos com nome, preço, quantidade e detalhes.
- **Edição de Produtos** – Permite modificar informações de produtos já cadastrados.
- **Remoção de Produtos** – Remove produtos do banco de dados.
- **Listagem de Produtos** – Recupera e exibe os produtos cadastrados.
- **Cadastro de Vendas** – Registra uma nova venda e atualiza o estoque automaticamente.
- **Listagem de Vendas** – Consulta todas as vendas realizadas.
- **Cadastro de Vendedores** – Cria contas de vendedores com login e senha.
- **Autenticação JWT** – Implementa segurança na API, garantindo acesso controlado a determinadas funcionalidades.

### **📌 Considerações Finais**
O TradeTrack é um projeto finalizado, mas aberto a melhorias futuras. Se tiver alguma sugestão ou encontrar algum problema, fique à vontade para abrir uma issue no repositório!
