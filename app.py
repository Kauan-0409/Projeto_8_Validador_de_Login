from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash
from banco import cadastrar_usuario, validar_login

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        nome = request.form['username']

        if validar_login(nome, request.form['password']):
            return 'Acesso Permitido!'

        else:
            return render_template('login.html', erro="Usuário ou senha incorretos!")


    return render_template('login.html')

@app.route('/cadastrar', methods=["POST", "GET"])
def cadastrar():
    if request.method == "POST":
        nome = request.form["username"]
        email = request.form["email"]
        senha = generate_password_hash(request.form["password"])

        cadastrar_usuario(nome, email, senha)

        return f'Cadastro concluído! Seja bem vindo {nome}!! {email} - {senha}' 
    return render_template('cadastrar.html')

if __name__ == "__main__":
    app.run(debug=True)