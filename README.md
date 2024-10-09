# Projeto de Cadastro de Usuário com FastAPI

## Descrição
Este projeto é uma API de cadastro de usuários construída com **FastAPI** e **SQLAlchemy**. Ele permite criar, ler, atualizar e excluir usuários, além de realizar a autenticação e gerenciamento de permissões de acesso.

---

## Instalação

### Pré-requisitos
- Python 3.7 ou superior
- Virtualenv (opcional, mas recomendado)

### Passo a Passo

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```
2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o servidor FastAPI

```bash
uvicorn main:app --reload
```

5. Acesse a documentação interativa da API no navegador:

* http://127.0.0.1:8000/docs (Swagger UI)
* http://127.0.0.1:8000/redoc (ReDoc)

## Estrutura do Projeto

### Principais Arquivos e Pastas

* **main.py**: Arquivo principal que contém as rotas da API.
* **crud.py**: Contém as funções de CRUD (Create, Read, Update, Delete) para manipulação dos dados de usuários.
* **models.py**: Define os modelos de dados utilizando SQLAlchemy.
* **schemas.py**: Define os esquemas de validação de dados utilizando Pydantic.
* **database.py**: Configura a conexão com o banco de dados SQLite.

--- 
## Referências
- [FastAPI - Documentação Oficial](https://fastapi.tiangolo.com/)
- [SQLAlchemy - Documentação Oficial](https://www.sqlalchemy.org/)
- [Pydantic - Documentação Oficial](https://pydantic-docs.helpmanual.io/)

--- 
## Autor
- **Nome**: Rafael Berçam Medeiros
- **Email**: rbercam.medeiros@gmail.com
- **GitHub**: [https://github.com/rafaelbercam](https://github.com/rafaelbercam)

--- 
## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

--- 
## Como Contribuir
Contribuições são bem-vindas! Siga os passos abaixo para colaborar com o projeto:

1. Faça um **fork** do projeto.
2. Crie uma nova branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça as alterações desejadas e adicione os commits:
   ```bash
    git commit -m "Adiciona nova feature"
   ```
4. Envie suas alterações para o repositório remoto:
    ```bash
    git push origin minha-feature
   ```
5. Abra um Pull Request no GitHub e descreva as mudanças propostas.