def exibir_numero(): 
    try:
        numero = input("Coloque um número para definir se é para ou impar: ")
        numero = int(numero)
        if numero % 2 == 0:
            print(f'O número {numero} é par')
        else:
            print(f'O número {numero} é impar')
    except:
        print("Digite um número válido")
