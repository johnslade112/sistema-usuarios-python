
import sqlite3

# conexão com o banco 
def conectar():
    return sqlite3.connect("usuarios.db")



# criando banco 
def criar_banco():
    conn = conectar()
    cursor = conn.cursor()

    # executando o comardo 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    email TEXT UNIQUE 
                   )""")

    # salvando e fechando a conversa com o banco 
    conn.commit()
    conn.close()



def inserir_usuario(nome, idade, email):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO usuarios(nome, idade,email)
    VALUES(?, ?, ?)
    """, (nome, idade, email))

    conn.commit()
    conn.close()
