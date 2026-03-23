# PROJETO
from time import sleep
from servico_usuario import numero_opcao_menu, criar_usuario, perguntar_continuar, listar_usuarios, buscar_usuario, remover_usuario
from database import carregar_dados

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
    
# função de entrada de dados
def obter_dado_usuario():
    nome = input("Nome: ").strip()
    idade = input("Idade: ")
    email = input("Email: ").strip()
    return nome, idade, email

# função principal
def main():
    while True:
        print("\n")
        print("=" * 50)
        print(" " * 6,"Sistema de Gerenciamento de Usuários")
        print("=" * 50)
        menu()
        opcao = numero_opcao_menu()

        # Criando usuário 
        if opcao == 1:
            while True:
                nome, idade, email = obter_dado_usuario()
                valido, resposta = criar_usuario(nome, idade, email)
                if not valido:
                    print(resposta)
                else:
                    print(resposta)
                if perguntar_continuar() == "N":
                    break
        
        #listando usuário
        elif opcao == 2:
            usuarios = listar_usuarios()
            for u in usuarios:
                print(f"ID: {u['id']} | Nome: {u['nome']} | Idade: {u['idade']} | Email: {u['email']}\n")


        # buscando usuário
        elif opcao == 3:
            try:
                numero_id = int(input("Digite o ID: "))
            except ValueError:
                print("ID inválido")
                continue
            valido, saida = buscar_usuario(numero_id)
            if not valido:
                print(saida)
            else:
                print("\n")
                print(f"ID: {saida['id']} | Nome: {saida['nome']} | Email: {saida['email']}")


        elif opcao == 4:
            try:
                id_remover = int(input("Digite o ID para remover usuário: "))
            except ValueError:
                print("ID inválido")
                continue
            valido, resposta = remover_usuario(id_remover)
            if not valido:
                print(resposta)
            else:
                print(resposta)

        # encerando o programa 
        else:
            print("Saindo...")
            sleep(3)
            print("FIM.")
            break
        
        
        
                

if __name__ == "__main__":
    main()


