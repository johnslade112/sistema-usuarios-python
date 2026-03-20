# PROJETO
from time import sleep
from servico_usuario import menu, num_opcao, criar_usuario, perguntar_continuar
from database import carregar_dados

# função principal
def main():
    lista_usuarios = carregar_dados()
    while True:
        print("\n")
        print("_________Sistema de gerenciamento de usuário_________")
        menu()
        opcao = num_opcao()
        if opcao == 1:
            while True:
                valido, dados = criar_usuario(lista_usuarios)
                if valido:
                    print(dados)
                else: 
                    print(dados)
                if perguntar_continuar() == "N":
                    break
            
        if opcao == 5:
            print("Saindo...")
            sleep(3)
            print("FIM.")
        
        
        
                

if __name__ == "__main__":
    main()


