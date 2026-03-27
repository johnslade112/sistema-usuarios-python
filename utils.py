



# função de que validar usuario
def validar_nome(nome):
    if nome == "":
        return False, "Nome não pode estar vazio\n"
    if len(nome) < 3:
        return False, "Nome deve possuir mais caracteres\n"
    return True,""

# validando idade
def validar_idade(idade):
    try:
        idade = int(idade)
    except ValueError:
        return False, "Idade deve ser numero\n"
    if idade <= 0:
        return False, "Idade inválida\n"
    return True, ""


# validando email
def validar_email(email):
    if email == "":
        return False, "Email vazio\n"
    
    if '@' not in email:
        return False, "Email inválido\n"
    return True, ""
 
