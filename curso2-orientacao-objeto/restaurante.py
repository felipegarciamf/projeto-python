class Restaurante:
    nome =  ''  
    categoria = ''
    ativo = False

    def init(self, nome, categoria, ativo):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo


restaurante_praca = Restaurante()
restaurante_praca.nome = 'Restaurante da Praça'
restaurante_praca.categoria = 'Comida Brasileira'
restaurante_praca.ativo = True


restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizzaria'
restaurante_pizza.categoria = 'Comida Italiana'
restaurante_pizza.ativo = False

restaurantes = [vars(restaurante_praca), vars(restaurante_pizza)]

print(restaurantes)