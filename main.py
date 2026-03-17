# PROJETO

import servico_usuario

# função principal
def main():
    while True:
        servico_usuario.menu()
        if servico_usuario.num_opcao() == 1:
            lista_usuarios = []
            while True:
                servico_usuario.criar_usuarios(lista_usuarios)
                if servico_usuario.perguntar_continuar() == "N":
                    continue

                
                

if __name__ == "__main__":
    main()


