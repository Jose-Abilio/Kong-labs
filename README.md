# Kong Labs - Flask + SQLAlchemy

Aplicação web simples usando Flask e SQLAlchemy para cadastro/login de usuários e CRUD de produtos. Projeto com foco educativo seguindo os requisitos: estrutura mínima (app, templates, static), persistência com SQLAlchemy (SQLite), autenticação básica por sessão, CRUD completo de produtos e templates Jinja2. Visual com tema preto e vermelho e logo da Kong Labs.

## Requisitos
- Python 3.10+
- Pip

## Instalação
1. (Opcional) Crie um ambiente virtual:
   - Windows PowerShell
     ```powershell
     python -m venv env
     .\\env\\Scripts\\Activate.ps1
     ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Executando o projeto
- Executar diretamente o app:
  ```bash
  python app.py
  ```
- Acesse em: http://127.0.0.1:5000/

Ao iniciar, o banco SQLite `kong_labs.db` será criado automaticamente na raiz do projeto.

## Estrutura de pastas
```
Kong-labs/
├─ app.py                   # App Flask + rotas + sessão + CRUD
├─ models.py                # Modelos SQLAlchemy (Usuario, Produto)
├─ templates/               # Templates Jinja2
│  ├─ base.html
│  ├─ index.html
│  ├─ login.html
│  ├─ cadastro_usuario.html
│  ├─ produtos.html
│  ├─ criar_produto.html
│  └─ editar_produto.html
├─ static/
│  ├─ css/
│  │  ├─ base.css           # Tema preto/vermelho
│  │  └─ inicial.css        # Estilos da home
│  └─ img/
├─ requirements.txt
└─ README.md
```

## Banco de Dados
- SQLite via SQLAlchemy.
- Models em `models.py`:
  - `Usuario`: id, nome, email (único), senha (hash), data_criacao
  - `Produto`: id, nome, preco (float), descricao, data_criacao

## Funcionalidades
- Cadastro de usuário: nome, e-mail, senha
- Login/Logout por sessão
- CRUD de produtos (após login):
  - Criar produto
  - Listar produtos
  - Editar produto
  - Excluir produto

## Rotas principais
- `GET /` – Home
- `GET|POST /cadastro_usuario` – Cadastro de usuário
- `GET|POST /login` – Login
- `GET /logout` – Logout
- `GET /produtos` – Listagem de produtos (requer login)
- `GET|POST /criar_produto` – Criar produto (requer login)
- `GET|POST /editar_produto/<id>` – Editar produto (requer login)
- `GET /excluir_produto/<id>` – Excluir produto (requer login)

## Logo e Tema
- Cores predominantes: preto e vermelho (ver `static/css/*.css`).
- Adicione a logo da Kong Labs em `static/img/kong-labs-logo.png`.
  - Caso o arquivo não exista, a home exibirá um espaço reservado.

## Notas
- Senhas são armazenadas com hash simples via Werkzeug (sem criptografia avançada; uso educativo).
- Sem relacionamentos entre usuários e produtos (independentes), conforme requisitos.

## Equipe
- Lucas Nobrega
- José Abílio
- Eduardo Vinícius
- Maria Luiza
