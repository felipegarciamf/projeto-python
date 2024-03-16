class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome} ({self._categoria} | {self.ativo})'
    

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(restaurante)

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'false'
    


restaurante_praca2 = Restaurante('Restaurante da Praça','Comida Brasileira')
restaurante_praca2._ativo = True
restaurante_praca2.listar_restaurantes()



restaurante_pizza2 = Restaurante('Pizzaria', 'Comida Italiana')
restaurante_pizza2.listar_restaurantes()

