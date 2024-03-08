class Restaurante:
    nome =  ''  
    categoria = ''
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.nome = 'Restaurante da Praça'
restaurante_praca.categoria = 'Comida Brasileira'
restaurante_praca.ativo = True


restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizzaria'
restaurante_pizza.categoria = 'Comida Italiana'
restaurante_pizza.ativo = False

restaurantes = [dir(restaurante_praca), dir(restaurante_pizza)]

print(restaurantes)