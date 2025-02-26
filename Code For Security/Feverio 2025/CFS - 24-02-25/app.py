from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/usuarios')
def usuarios():
    return 'Usuarios'

@app.route('/usuarios/inserir')
def usuarios_inserir():
    return render_template('inserir.html')

@app.route('/usuarios/cadastro', methods=['POST'])
def usuarios_cadastro():
    nome = requests.form['nome']
    email = requests.form['email']

    return render_template('usuarios.html', nome=nome, email=email)