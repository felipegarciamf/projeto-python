class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome} ({self._categoria} | {self.ativo})'
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(restaurante)

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'false'

restaurante_praca2 = Restaurante('Restaurante da Praça','Comida Brasileira')
restaurante_praca2._ativo = True

restaurante_pizza2 = Restaurante('Pizzaria', 'Comida Italiana')

Restaurante.listar_restaurantes()

