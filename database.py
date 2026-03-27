
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


def listar_usuario():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    """)
    usuarios = cursor.fetchall()

    conn.close()
    return usuarios


def buscar_usuario(id_busca):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM usuarios WHERE id = ?
    """, (id_busca,))
    usuario = cursor.fetchone()

    conn.close()
    return usuario
    

def remover_usuario(id_remover):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM usuarios WHERE id = ?', (id_remover,))
    usuario_removido = cursor.rowcount
    conn.commit()
    conn.close
    return usuario_removido


