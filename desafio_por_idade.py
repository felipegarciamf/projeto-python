

def validarIdade():
    if idade <= 12:
        print("Você é criança")
    elif idade <= 18:
        print("Você é adolescente")
    else:
        print("Você é adulto")


idade = input("Digite a sua idade: ")
idade = int(idade)

validarIdade()