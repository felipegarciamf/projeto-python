def validar_idade():
    try:
        idade = input("Digite a sua idade: ")
        idade = int(idade)
        if idade <= 12:
            print("Você é criança")
        elif idade <= 18:
            print("Você é adolescente")
        else:
            print("Você é adulto")
    except:
        print("Digite uma idade válida")


