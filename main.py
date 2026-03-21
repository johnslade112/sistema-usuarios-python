# PROJETO
from time import sleep
from servico_usuario import menu, numero_opcao_menu, criar_usuario, perguntar_continuar, listar_usuarios, buscar_usuario, remover_usuario
from database import carregar_dados

# função principal
def main():
    lista_usuarios = carregar_dados()
    while True:
        print("\n")
        print("_________Sistema de gerenciamento de usuário_________")
        menu()
        opcao = numero_opcao_menu()

        # Criando usuário 
        if opcao == 1:
            while True:
                valido, resposta = criar_usuario(lista_usuarios)
                if not valido:
                    print(resposta)
                print(resposta)
                if perguntar_continuar() == "N":
                    break
        
        #listando usuário
        elif opcao == 2:
            usuarios = listar_usuarios(lista_usuarios)
            for u in usuarios:
                print(f"ID: {u['id']} | Nome: {u['nome']} | Idade: {u['idade']} | Email: {u['email']}\n")


        # buscando usuário
        elif opcao == 3:
            try:
                numero_id = int(input("Digite o ID: "))
            except ValueError:
                print("ID inválido")
                continue
            valido, saida = buscar_usuario(lista_usuarios, numero_id)
            if not valido:
                print(saida)
            print(f"ID: {saida['id']} | Nome: {saida['nome']} | Email: {saida['email']}")


        elif opcao == 4:
            try:
                id_remover = int(input("Digite o ID para remover usuário: "))
            except ValueError:
                print("ID inválido")
                continue
            valido, resposta = remover_usuario(lista_usuarios, id_remover)
            if not valido:
                print(resposta)
            print(resposta)

        # encerando o programa 
        else:
            print("Saindo...")
            sleep(3)
            print("FIM.")
            break
        
        
        
                

if __name__ == "__main__":
    main()


