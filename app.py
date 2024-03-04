import os
import desafio_par_impar
import desafio_por_idade
import desafio_logon



def exibir_nome_do_programa():
    print("hello world")


def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar Restaurantes")

def finalizarApp():
    print('Finalizando aplicação')
    os.system('clear')

def opcaoInvalida():
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
        elif opcao_escolhida == 2:
            print('Listar Restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar Restaurantes')
        elif opcao_escolhida == 4:
            finalizarApp()
        else:
            opcaoInvalida()
    except:
        opcaoInvalida()


def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    desafio_par_impar.exibirNumero()
    desafio_por_idade.validarIdade()
    desafio_logon.logarUsuario()




if __name__ == "__main__":
   main()