

def exibirNumero(): 
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é impar')


numero = input("Coloque um número para definir se é para ou impar: ")
numero = int(numero)

exibirNumero()