class Restaurante:

    restaurantes = []


    def __init__(self, nome, categoria, ativo):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self.nome} ({self.categoria})'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(restaurante)




restaurante_praca2 = Restaurante('Restaurante da Praça','Comida Brasileira', True)

restaurante_pizza2 = Restaurante('Pizzaria', 'Comida Italiana', False)


Restaurante.listar_restaurantes()
