class Restaurante:
    def __init__(self, nome, categoria, ativo):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo



    nome =  ''  
    categoria = ''
    ativo = False



restaurante_praca2 = Restaurante('Restaurante da Praça','Comida Brasileira', True)

restaurante_pizza2 = Restaurante('Pizzaria', 'Comida Italiana', False)

restaurantes2 = [vars(restaurante_praca2), vars(restaurante_pizza2)]

print(restaurantes2)
