from flask import Flask, render_template, request, redirect, session, make_response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'minhachavesecreta'

lista_usuarios = [
    {'nome':'Sarah Lima', 'email':'sarah123@gmail.com', 'funcao': 'Designer'}
]

# lista_usuarios = []

@app.route('/')
def index():
    if 'nome' in session:
        titulo = f'Bem vindo, {session['nome']}!'
    else:
        titulo = f'Bem vindo, visitante!'
    # return render_template('Index.html', titulo=titulo)
    # html = render_template('index.html', titulo=titulo)
    # resposta = make_response(html)
    # resposta.status_code = 202
    # resposta.set_cookie('username', 'jam423')
    # resposta.set_cookie('visitas', '1')


    html = render_template('index.html', titulo=titulo)
    resposta = make_response(html)

    if not request.cookies.get('nome'):
        resposta.status_code = 202
        resposta.set_cookie('username', 'jam423')
        resposta.set_cookie('visitas', '1')
    else:
        visitas = int(request.cookies.get('visistas') + 1)
        resposta.set_cookie('visitas', visitas)
    return resposta

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/usuarios/inserir')
def usuarios_inserir():
    return render_template('inserir.html')

@app.route('/usuarios/cadastro', methods=['POST'])
def usuarios_cadastro():
    novo_usuario = dict()
    novo_usuario['nome'] = request.form.get('nome')
    novo_usuario['email'] = request.form.get('email')
    novo_usuario['funcao'] = request.form.get('funcao')

    lista_usuarios.append(novo_usuario)

    return redirect('/usuarios')

@app.route('/criar_sessao')
def criar_sessao():
    session['nome'] = 'James'
    session['userID'] = '14325igsd'
    return 'Criou Sessão'

@app.route('/limpar_sessao')
def limpar_sessao():
    session.clear()
    return 'Limpou Sessão'