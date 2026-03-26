from utils import validar_nome, validar_idade, validar_email
from database import inserir_usuario


def validar_dados(nome, idade, email):
    valido, saida = validar_nome(nome)
    if not valido:
        return False, saida
    
    valido, saida = validar_idade(idade)
    if not valido:
        return False, saida
    
    valido, saida = validar_email(email)
    if not valido:
        return False, saida
    return True, (nome, int(idade), email)



def criar_usuario(nome, idade, email):
    valido, reposta_ou_dados = validar_dados(nome, idade, email)
    if not valido:
        return False, reposta_ou_dados
    
    nome, idade, email = reposta_ou_dados
    try:
        inserir_usuario(nome, idade, email)
    except:
        return False, "Email já existe"
    return True, "Usuário cadastrado com sucesso\n"



