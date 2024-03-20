from modelos.restaurante import Restaurante


def cadastrar_restaurante(nome, categoria):
    restaurante_praca2 = Restaurante(nome, categoria)
    restaurante_praca2.alterar_status()
    restaurante_praca2.adicionar_avaliacao("jorge", 3)
    restaurante_praca2.adicionar_avaliacao("Joana dark", 3)
    restaurante_praca2.adicionar_avaliacao("Chico Boarque", 5)
    restaurante_praca2.listar_restaurantes()


def main():
    cadastrar_restaurante('Restaurante da Praça','Comida Brasileira')
    

if __name__ == '__main__':
    main()

