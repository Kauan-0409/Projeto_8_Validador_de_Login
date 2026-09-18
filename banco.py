from werkzeug.security import check_password_hash
import sqlite3

nome = "usuarios.db"

script_tabela = """CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                senha TEXT NOT NULL
            );"""
            
try:
    with sqlite3.connect(nome) as conn:
        # Cria um cursor
        cur = conn.cursor()

        # Executa o script
        cur.execute(script_tabela)

        # Salva as alterações no banco de dados
        conn.commit()

        print("Tabelas Criadas com Sucesso")
except sqlite3.OperationalError as e:
    print("ERRO: ", e)

def cadastrar_usuario(nome_usuario, email, senha):
    sql = "INSERT INTO usuarios (nome, email, senha) VALUES (?,?,?)"

    try:
        with sqlite3.connect(nome) as conn:
                
            # Cria um cursor
            cur = conn.cursor()

            # Executa o script
            cur.execute(sql, (nome_usuario, email, senha))

            # Salva as alterações no banco de dados
            conn.commit()

    except sqlite3.OperationalError as e:
        print("ERRO: ", e)


        def validar_login(nome_usuario, senha):
            usuario = consultar_usuario(nome_usuario)
            if usuario:
                return check_password_hash(usuario['senha'], senha)
            else:
                return False

def consultar_usuario(nome_usuario):
    scrypt_consulta_usuario = "SELECT * FROM usuarios WHERE nome = ?"

    try:
        with sqlite3.connect(nome) as conn:
            conn.row_factory = sqlite3.Row
            # Cria um cursor
            cur = conn.cursor()
            

            # Executa o script
            cur.execute(scrypt_consulta_usuario, (nome_usuario,))
            res = cur.fetchone() # retorna uma lista de listas

            return res
    except sqlite3.OperationalError as e:
        print("ERRO: ", e)

def validar_login(nome_usuario, senha):
    usuario = consultar_usuario(nome_usuario)
    if usuario:
        return check_password_hash(usuario['senha'], senha)
    else:
        return False