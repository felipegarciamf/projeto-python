import os
import desafio_par_impar
import desafio_por_idade
import desafio_logon


restaurantes = ['pizza', 'lasanha', 'macarrão', 'sushi', 'hamburguer', 'churrasco', 'feijoada', 'strogonoff', 'peixe', 'frango']


def exibir_nome_do_programa():
    print("hello world")


def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar Restaurantes")

def finalizar_app():
    print('Finalizando aplicação')
    os.system('clear')

def opcao_invalida():
    print('Opção inválida')
    os.system('clear')

def escolher_opcao():
    try:
        opcao_escolhida = input('Digite a opção desejada: ')
        opcao_escolhida = int(opcao_escolhida)
        print(opcao_escolhida == 1)
        print (type(opcao_escolhida))
        print(type(1))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            print('Cadastrar Restaurante')
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('Listar Restaurantes')
            print('vai se foder')
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurantes')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_novo_restaurante():
    os.system('clear')
    print('Cadastrar novo restaurante')
    nome = input('Digite o nome do restaurante: ')
    restaurantes.append(nome)
    print(f'Restaurante cadastrado com sucesso {restaurantes}')
    input('Pressione enter para continuar')
    main()

def listar_restaurantes():
    os.system('clear')
    print('Listar restaurantes')
    for restaurante in restaurantes:
        print(f'Nome: {restaurante}')

    input('Pressione enter para continuar')
    main()


def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    desafio_par_impar.exibir_numero()
    desafio_por_idade.validar_idade()
    desafio_logon.logar_usuario()




if __name__ == "__main__":
   main()