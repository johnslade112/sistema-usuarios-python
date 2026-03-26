

# JSON
import sqlite3
import json

# função que carrega dados do JSON para python
def carregar_dados():
    try:
        # abre o arq, tranforma json -> python
        with open("usuarios.json", "r") as f:
            # conversão de conteudo para python
            return json.load(f)
    # retorna lista vazia caso não encontre o arquivo
    except FileNotFoundError:
        return []
    
# função que salva tudo para JSON
def salvar_dados(lista_usuarios):
    # abre o arq, ler e sobrescreve
    with open("usuarios.json", "w") as f:
        json.dump(lista_usuarios, f, indent=4)



# SQLite
# coneção com o banco 
def conectar():
    return sqlite3.connect("usuarios.db") 

#criando tabela
def criar_tabela():
    # abre conexão
    conn = conectar()
    # prepara pra executar
    cursor = conn.cursor()

    # executando comando SQL
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER, 
        email TEXT UNIQUE
    )
    """)
    # salvando banco
    conn.commit()
    # fecha conexão
    conn.close()







def inserir_usuarios(nome, idade, email):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO usuarios (nome, idade, email)
    VALUES (?, ?, ?)
    """, (nome, idade, email))

    conn.commit()
    conn.close()



def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM usuarios""")
    usuarios = cursor.fetchall()

    conn.close()
    return usuarios


def buscar_usuario(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM usuarios WHERE id = ?
    """, (id,))

    usuario = cursor.fetchone()

    conn.close()
    return usuario


def remover_usuario(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM usuarios WHERE id = ?
    """,(id,))

    deletado = cursor.rowcount

    conn.commit()
    conn.close()
    return deletado