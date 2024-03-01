import os

print("hello world")

print("1. Cadastrar Restaurante")

print("2. Listar Restaurantes")
print("3. Ativar Restaurantes")

opcao_escolhida = input('Digite a opção desejada: ')
opcao_escolhida = int(opcao_escolhida)
print(opcao_escolhida == 1)
print (type(opcao_escolhida))
print(type(1))

print('Você escolheu a seguinte opção', opcao_escolhida)

print(f'Você escolheu a opção {opcao_escolhida}')



def finalizarApp():
    os.system('clear')
    print('Finalizando aplicação')



if opcao_escolhida == '1':
    print('Cadastrar Restaurante')
elif opcao_escolhida == '2':
    print('Listar Restaurantes')
elif opcao_escolhida == '3':
    print('Ativar Restaurantes')
else :
    finalizarApp()