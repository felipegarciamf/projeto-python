from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato



bebida = Bebida('Coca-cola', 5.0, '600ml')
prato = Prato('Feijoada', 30.00, 'Feijoada completa')

restaurante_praca = Restaurante('Restaurante da Praça','Comida Brasileira')

restaurante_praca.adicionar_no_cardapio(bebida)
restaurante_praca.adicionar_no_cardapio(prato)



def main():
    restaurante_praca.exibir_cardapio
    

if __name__ == '__main__':
    main()

