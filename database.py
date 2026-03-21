import json



def carregar_dados():
    try:
        # abre o arq, tranforma json -> python
        with open("usuarios.json", "r") as f:
            # conversão de conteudo para python
            return json.load(f)
    # retorna lista vazia caso não encontre o arquivo
    except FileNotFoundError:
        return []
    

def salvar_dados(lista_usuarios):
    # abre o arq, ler e sobrescreve
    with open("usuarios.json", "w") as f:
        json.dump(lista_usuarios, f, indent=4)