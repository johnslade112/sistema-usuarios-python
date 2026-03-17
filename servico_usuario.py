# PROJETO
print("Sistemas de gerenciamento de Usuários")




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
# função de perguntar se quer continuar
def perguntar_continuar():
    while True:
        resposta = input("Quer adicionar mais usuário [S/N]: ").upper().strip()
        print("")
        if resposta in ("S","N"):
            return resposta
        print("Entrado inválida, deve ser [S/N].\n")

# função de criar usuarios
def criar_usuario(lista_usuarios):
    cont = len(lista_usuarios) + 1
    usuario = {
        "id": cont,
        "nome": input("Nome: "),
        "idade": int(input("Idade: ")),
        "email": input("Email: ")
    }
    lista_usuarios.append(usuario)
    print("Usuário criado com Sucesso\n")

# função da escolha da opção  
def num_opcao():
    while True:
        try:
            opcao = int(input("Numero da Opção: "))
            print("\n")
            if opcao in (1, 2, 3, 4, 5):
                return opcao
            print("Entrada inválida, deve ser de 1-5")
        except ValueError as erro:
            print("Digite apenas numeros.\n")







