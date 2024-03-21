from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
        self.avalicao = []


    def __str__(self):
        return f'{self._nome} ({self._categoria} | {self._ativo})'
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(restaurante, f'Média de avaliação: {restaurante.media_avaliacao}')

            for avaliacao in restaurante.avalicao:
                print(avaliacao)


    def alterar_status(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'false'
    
    def adicionar_avaliacao(self, nome, nota):
        avaliacao = Avaliacao(nome, nota)
        self.avalicao.append(avaliacao)


    @property
    def media_avaliacao(self):
        soma = 0
        for avaliacao in self.avalicao:
            soma += avaliacao.nota
        return soma / len(self.avalicao)
        
