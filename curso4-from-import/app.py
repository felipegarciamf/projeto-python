from modelos.resturante import Restaurante


def cadastrar_restaurante(nome, categoria):
    restaurante_praca2 = Restaurante(nome, categoria)
    restaurante_praca2.alterar_status()


def main():
    cadastrar_restaurante('Restaurante da Praça','Comida Brasileira')

if __name__ == '__main__':
    main()

