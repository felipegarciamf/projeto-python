import os



def exibir_nome_do_programa():
    print("hello world")


def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar Restaurantes")

def finalizarApp():
    print('Finalizando aplicação')
    os.system('clear')


def escolher_opcao():
    opcao_escolhida = input('Digite a opção desejada: ')
    opcao_escolhida = int(opcao_escolhida)
    print(opcao_escolhida == 1)
    print (type(opcao_escolhida))
    print(type(1))
    print(f'Você escolheu a opção {opcao_escolhida}')

    if opcao_escolhida == 1:
        print('Cadastrar Restaurante')
    elif opcao_escolhida == 2:
        print('Listar Restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar Restaurantes')
    else :
        finalizarApp()


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
   main()