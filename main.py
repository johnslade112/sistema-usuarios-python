from database import criar_banco
from service import criar_usuario






# função de menu
def menu():
    print("""
            Gerenciamento de usuarios
          
            1 - Cadastrar usuario
            2 - Listar usuario
            3 - Buscar usuario
            4 - Remover usuario
            5 - Sair
    """)

# função para obter os dados 
def obter_dados_usuario():
    nome = input("Nome: ").strip()
    idade = input("Idade: ").strip()
    email = input("Email: ").strip()
    return nome, idade, email


# função de menu de escoha
def num_menu_escolha():
    while True:
        try:
            num = int(input("Numero da opção: "))
            print("\n")
            if num not in (1, 2, 3, 4, 5):
                print("Opção não existe no menu\n")
            return num
        except ValueError:
            print("Numero dever inteiro\n")



def continuar_S_N():
    while True:
        print("")
        continuar = input("Quer adicionar mais um usuário?[S/N]: ").upper().strip()
        print("\n")
        if continuar in ("S", "N"):
            return continuar
        print("Deve ser Sim[S] ou Não[N]\n")


# 
def main():
    criar_banco()
    while True:
        menu()
        opcao = num_menu_escolha()
        if opcao == 1:
            while True:
                nome, idade, email = obter_dados_usuario()
                valido, resposta_ou_dados = criar_usuario(nome, idade, email)
                if not valido:
                    print(resposta_ou_dados)
                else:
                    print(resposta_ou_dados)
                if continuar_S_N() == "N":
                    break
        if opcao == 5:
            break





    
    
    



# controlando execuções
# evitando execuções automáticas 
if __name__ == "__main__":
    main()
    