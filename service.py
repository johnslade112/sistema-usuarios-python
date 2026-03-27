from utils import validar_nome, validar_idade, validar_email
from database import inserir_usuario, listar_usuario, buscar_usuario, remover_usuario

# função de validar dados
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


# função de criar os usuarios
def criar_usuario(nome, idade, email):
    valido, reposta_ou_dados = validar_dados(nome, idade, email)
    if not valido:
        return False, reposta_ou_dados
    
    nome, idade, email = reposta_ou_dados
    try:
        inserir_usuario(nome, idade, email)
    except:
        return False, "Email já existe"
    return True, "Usuário cadastrado com sucesso!\n"


# função de listar usuá rios
def listar_usuario_service():
    return listar_usuario()


# função de buscar usuários
def buscar_usuario_service(id):
    usuario = buscar_usuario(id)
    if not usuario:
        return False, "Usuário não existe\n"
    return True, usuario


def remover_usuario_servico(id):
    usuario = remover_usuario(id)
    if usuario == 0:
        return False, "Usuário não existe\n"
    return True, "Usuário removido com sucesso!\n"