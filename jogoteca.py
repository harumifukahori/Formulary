from flask import Flask, render_template, request, redirect, session, flash, url_for


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('FFXIV', 'MMORPG', 'PC')
jogo2 = Jogo('Valorant', 'FPS', 'PC')
jogo3 = Jogo('League', 'MOBA', 'PC')
lista = [jogo1, jogo2, jogo3]


class Usuario:
    def __init__(self, nome, username, senha):
        self.nome = nome
        self.username = username
        self.senha = senha


usuario1 = Usuario("Harumi T", "Haru", "alohomora")
usuario2 = Usuario("Khaleesi", "Kha", "dracarys")
usuario3 = Usuario("Yshtola", "BlackMage", "lahi")

usuarios = {usuario1.username: usuario1,
            usuario2.username: usuario2,
            usuario3.username: usuario3}

app = Flask(__name__)
app.secret_key = 'japao'


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        session['usuario_logado'] = request.form['usuario']

        if request.form['senha'] == usuario.senha:
            flash(usuario.username + ' logado com sucesso!')
        return redirect(url_for('novo'))
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


app.run(debug=True)
