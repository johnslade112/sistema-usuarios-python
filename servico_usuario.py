from utilidades import obter_dado_usuario, validar_nome, validar_idade, validar_email
from database import salvar_dados, carregar_dados


# função menu
def menu():
    print("""
                Sistema de Usuários

                1 - Criar usuário
                2 - Listar usuários
                3 - Buscar usuário
                4 - Remover usuário
                5 - Sair
        \n
        """)


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
def validar_usuario(nome, idade, email, lista_usuarios):
    valido, erro = validar_nome(nome)
    # se não for True
    if not valido:
        return False, erro

    valido, erro = validar_idade(idade)
    if not valido:
        return False, erro
    
    valido, erro = validar_email(email, lista_usuarios)
    if not valido:
        return False, erro
    
    return True, "", (nome, int(idade), email)



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

# função de salvar usuários
def salvar_usuario(usuario, lista_usuarios):
    lista_usuarios.append(usuario)
    salvar_dados(lista_usuarios)


# função de usuario
def criar_usuario(lista_usuarios):
    # entrado de dados
    nome, idade, email = obter_dado_usuario()
    
    # validando os dados 
    valido, resposta, dados = validar_usuario(nome, idade, email, lista_usuarios)
    if not valido:
        return False, resposta
    
    nome, idade, email = dados
    # gerando_id 
    novo_id = gerar_id(lista_usuarios)
    # montando 
    usuario = montar_usuario(novo_id, nome, idade, email)

    #salvando
    salvar_usuario(usuario, lista_usuarios)
    return True, "Usuário cadastrado com sucesso!\n"

    

    
# função de listar os usuários
def listar_usuarios(lista_usuarios):
    return lista_usuarios


# função de buscar usuário pelo ID
def buscar_usuario(lista_usuarios, numero_id):
    for usuario in lista_usuarios:
        if usuario["id"] == numero_id:
            return True, usuario
    return False, "Usuário não encontrado.\n"


# função de remover usuário
def remover_usuario(lista_usuarios, id_remover):
    for usuario in lista_usuarios:
        if usuario["id"] == id_remover:
            lista_usuarios.remove(usuario)
            salvar_dados(lista_usuarios)
            return True, "Usuário removido com sucesso!\n"
    return False, "Usuário não encontrado.\n"












