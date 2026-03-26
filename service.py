from utils import  validar_nome, validar_idade, validar_email
from database import inserir_usuarios, listar_usuarios, buscar_usuario, remover_usuario



# função de função        
def numero_opcao_menu():
    while True:
        try:
            opcao = int(input("Numero da Opção: "))
            print("\n")
            if opcao in (1, 2, 3, 4, 5):
                return opcao
            print("Entrada inválida, deve ser de 1-5")
        except ValueError as erro:
            print("Digite apenas numeros.\n")

# função de perguntar se quer continuar
def perguntar_continuar():
    while True:
        resposta = input("Quer adicionar mais usuário [S/N]: ").upper().strip()
        print("")
        if resposta in ("S","N"):
            return resposta
        print("Entrado inválida, deve ser [S/N].\n")


# função de validar usuários 
def validar_usuario(nome, idade, email):
    valido, erro = validar_nome(nome)
    # se não for True
    if not valido:
        return False, erro

    valido, erro = validar_idade(idade)
    if not valido:
        return False, erro
    
    valido, erro = validar_email(email)
    if not valido:
        return False, erro
    
    return True, (nome, int(idade), email)



# função de gerar ID
def gerar_id(lista_usuarios):
    if not lista_usuarios:
        return 1
    # isso soma faz a soma com o maior id da lista
    return max(u["id"] for u in lista_usuarios) + 1


    

# função de gerar id
def montar_usuario(id, nome, idade, email):
    return {
        "id": id,
        "nome": nome,
        "idade": int(idade),
        "email": email
    }



# função de usuario
def criar_usuario(nome, idade, email):
    # validando os dados 
    valido, resposta_ou_dados = validar_usuario(nome, idade, email)
    if not valido:
        return False, resposta_ou_dados
    nome, idade, email = resposta_ou_dados
    try:
        inserir_usuarios(nome, idade, email)
    except:
        return True, "Email já foi cadastrado\n"
    
    return True, "Usuário cadastrado com sucesso!\n"



# função de listar os usuários
def listar_usuarios_service():
    return listar_usuarios()


# função de buscar usuário pelo ID
def buscar_usuario_service(numero_id):
    usuario = buscar_usuario(numero_id)
    if usuario is None:
        return False, "Usuário não existe\n"
    return True, usuario


    

# função de remover usuário
def remover_usuario_service(id_remover):
    deletado = remover_usuario(id_remover)
    if deletado == 0:
        return True, "Usuário não encontrado\n"
    return False, "Usuário removido com sucesso!\n    "













