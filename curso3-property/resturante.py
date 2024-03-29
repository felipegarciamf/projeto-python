class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome} ({self._categoria} | {self._ativo})'
    

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(restaurante)

    def alterar_status(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'false'
    


restaurante_praca2 = Restaurante('Restaurante da Praça','Comida Brasileira')
restaurante_praca2.alterar_status()



restaurante_pizza2 = Restaurante('Pizzaria', 'Comida Italiana')

restaurante_pizza2.listar_restaurantes()

