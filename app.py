from flask import Flask, render_template
from flask import request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro_usuario', methods=['POST,GET'])
def cadastro_usuario():
    if request.method == 'POST':
        
        pass
    return render_template('cadastro_usuario.html')

@app.route('/login', methods=['POST,GET'])
def login():
    if request.method == 'POST':
        
        pass
    return render_template('login.html')