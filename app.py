from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

from infra.repository.produts_repo import ProdutosRepository
from infra.repository.users_repo import UsersRepository
from infra.configs.connection import DBConnectionHandler

prod_repo = ProdutosRepository()
user_repo = UsersRepository() 

app = Flask(__name__)

# Configurações
app.config['SECRET_KEY'] = 'kong-labs-secret-key-2024'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro_usuario', methods=['GET', 'POST'])
def cadastro_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        # Verificar se o email já existe
        usuario_existente = user_repo.select(email)
        if usuario_existente:
            flash('Email já cadastrado!', 'error')
            return render_template('cadastro_usuario.html')
        
        # Criar novo usuário
        senha_hash = generate_password_hash(senha)
        
        try:
            user_repo.insert(nome, email, senha_hash)
            flash('Usuário cadastrado com sucesso!', 'success')
            return redirect(url_for('login'))
        except:
            flash('Erro ao cadastrar usuário!', 'error')
            return render_template('cadastro_usuario.html')
    
    return render_template('cadastro_usuario.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        usuario = user_repo.select(email)
        
        if usuario and check_password_hash(usuario.user_senha, senha):
            session['user_id'] = usuario.user_id
            session['user_nome'] = usuario.user_nome
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('produtos'))
        else:
            flash('Email ou senha incorretos!', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('index'))

@app.route('/produtos')
def produtos():
    if 'user_id' not in session:
        flash('Você precisa fazer login primeiro!', 'error')
        return redirect(url_for('login'))
    
    produtos = prod_repo.select_all()
    return render_template('produtos.html', produtos=produtos)

@app.route('/criar_produto', methods=['GET', 'POST'])
def criar_produto():
    if 'user_id' not in session:
        flash('Você precisa fazer login primeiro!', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        descricao = request.form['descricao']
                
        try:
            prod_repo.insert(nome, preco, descricao)
            flash('Produto criado com sucesso!', 'success')
            return redirect(url_for('produtos'))
        except:
            flash('Erro ao criar produto!', 'error')
    
    return render_template('criar_produto.html')

@app.route('/editar_produto/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
    if 'user_id' not in session:
        flash('Você precisa fazer login primeiro!', 'error')
        return redirect(url_for('login'))
    
    produto = prod_repo.select(id)
    
    if request.method == 'POST':
        if produto:
            try:
                prod_repo.update(id=id, nome=request.form['nome'], preco=request.form['preco'], descricao=request.form['descricao'])
                flash('Produto atualizado com sucesso!', 'success')
                return redirect(url_for('produtos'))
            
            except:
                flash('Erro ao atualizar produto!', 'error')
    
    return render_template('editar_produto.html', produto=produto)

@app.route('/excluir_produto/<int:id>')
def excluir_produto(id):
    if 'user_id' not in session:
        flash('Você precisa fazer login primeiro!', 'error')
        return redirect(url_for('login'))
    
    produto = prod_repo.select(id)
    
    if produto:
        try:
            prod_repo.delete(id)
            flash('Produto excluído com sucesso!', 'success')

        except:
            flash('Erro ao excluir produto!', 'error')
    
    return redirect(url_for('produtos'))

if __name__ == '__main__':
    db_conn = DBConnectionHandler()
    db_conn.create_db_tables()
    app.run(debug=True)