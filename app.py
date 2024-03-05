import os
import desafio_par_impar
import desafio_por_idade
import desafio_logon


restaurantes = [{'nome' : 'restaurante1', 'ativo': True}, {'nome' : 'restaurante2', 'ativo': False}]


def voltar_ao_menu_principal():
    input('Pressione uma tecla para voltar ao menu ')
    main()

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
    voltar_ao_menu_principal()

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
            voltar_ao_menu_principal()
    except:
        opcao_invalida()
        voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar Restaurante')
    nome = input('Digite o nome do restaurante: ')
    restaurantes.append(nome)
    print(f'Restaurante cadastrado com sucesso {restaurantes}')
    voltar_ao_menu_principal()
    

def listar_restaurantes():
    os.system('clear')
    print('Listar restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        ativo = restaurante['ativo']
        print(f'Nome do restaurante: {nome_restaurante} - Ativo: {ativo}')
    voltar_ao_menu_principal()


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