from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import db, Usuario, Produto
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configurações
app.config['SECRET_KEY'] = 'kong-labs-secret-key-2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kong_labs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar extensões
db.init_app(app)

# Criar tabelas
with app.app_context():
    db.create_all()

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
        usuario_existente = Usuario.query.filter_by(email=email).first()
        if usuario_existente:
            flash('Email já cadastrado!', 'error')
            return render_template('cadastro_usuario.html')
        
        # Criar novo usuário
        senha_hash = generate_password_hash(senha)
        novo_usuario = Usuario(nome=nome, email=email, senha=senha_hash)
        
        try:
            db.session.add(novo_usuario)
            db.session.commit()
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
        
        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario and check_password_hash(usuario.senha, senha):
            session['user_id'] = usuario.id
            session['user_nome'] = usuario.nome
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
    
    produtos = Produto.query.all()
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
        
        novo_produto = Produto(nome=nome, preco=preco, descricao=descricao)
        
        try:
            db.session.add(novo_produto)
            db.session.commit()
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
    
    produto = Produto.query.get_or_404(id)
    
    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.preco = float(request.form['preco'])
        produto.descricao = request.form['descricao']
        
        try:
            db.session.commit()
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
    
    produto = Produto.query.get_or_404(id)
    
    try:
        db.session.delete(produto)
        db.session.commit()
        flash('Produto excluído com sucesso!', 'success')
    except:
        flash('Erro ao excluir produto!', 'error')
    
    return redirect(url_for('produtos'))

if __name__ == '__main__':
    app.run(debug=True)