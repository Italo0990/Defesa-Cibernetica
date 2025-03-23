from flask import Flask, render_template, request, redirect
from flask import session, make_response, flash, render_template_string
from flask_wtf import CSRFProtect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'minhachavesupersecreta'

csrf = CSRFProtect(app)

# lista_usuarios = [
#     {'nome':'Sarah Lima', 'email':'sarah123@email.com', 'funcao':'Design'}
# ]
lista_usuarios = []


@app.route('/')
def index():
    if 'nome' in session:
        titulo = f"Bem vindo {session['nome']}"
    else:
        titulo = f'Bem vindo visitante'
    #return render_template('index.html', titulo=titulo)    
    #mensagem antes da resposta
    flash('Bem vindo ao Flash!', 'primary')

    html = render_template('index.html', titulo=titulo)
    resposta = make_response(html)
    resposta.status_code = 202
    resposta.set_cookie('username','godo123')
    if not request.cookies.get('visitas'):
        resposta.set_cookie('visitas','1')
    else:
        visitas = int(request.cookies.get('visitas')) + 1
        resposta.set_cookie('visitas',str(visitas))
       
    return resposta

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)
    # html = '<tables>'
    # for user in lista_usuarios:
    #     html += f'''
    #      <tr>
    #      <td>{user['nome']}</td>
    #      <td>{user['email']}</td>
    #      <td>{user['funcao']}</td>
    #      <tr>
    # '''     
    # return html

@app.route('/usuarios/inserir')
def usuarios_inserir():
    return render_template('inserir.html')

@app.route('/usuarios/cadastro', methods=['POST'])
def usuarios_cadastro():
    novo_usuario = dict()

    for chave, valor in request.form.items():
        if not valor:
            flash(f"Falha - O campo {chave} é obrigatório!", "danger")
            return redirect('/usuarios/inserir')

    nome = request.form.get('nome')

    if not nome or not isinstance(nome, str):
        flash("Falha - Nome inválido!", "danger")
        return redirect('/usuarios/inserir')
    else:
        novo_usuario['nome'] = nome

    novo_usuario['email'] = request.form.get('email')

    funcoes = ['dev', 'gerente', 'design', 'cyber']

    if request.form.get('funcao') not in funcoes:
        flash("Falha - Função inválida!", "danger")
        return redirect('/usuarios/inserir')
    else:
        novo_usuario['funcao'] = request.form.get('funcao')

    try:
        lista_usuarios.append(novo_usuario)
        flash('Usuário inserido com sucesso', 'success')
        return redirect('/usuarios')
    except:
        flash('Falha na inserção do usuário', 'danger')
        return redirect('/usuarios/inserir')

    
    #return render_template('usuarios.html', lista_usuarios)

@app.route('/criar_sessao')
def criar_sessao():
    session['nome'] = 'Godofredo'
    session['userid'] = '1234adfs'

    return 'Criou sessao'
    
@app.route('/limpar_sessao')
def limpar_sessao():
    session.clear()
    return 'Limpou sessao'

# @app.route('/upload')
# def upload():
#     return render_template('upload.html')

@app.route('/upload_arq', methods=['GET', 'POST'])
def upload_arq():
    if request.method == 'GET':
        return render_template('upload.html')
    if request.method == 'POST':
        f = request.files['arquivo']
        f.save(f.filename)

    flash('Arquivo deu certo', 'suecces')
    return render_template('upload.html')