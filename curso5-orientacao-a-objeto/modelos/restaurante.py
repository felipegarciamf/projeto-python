from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
        self.avalicao = []
        self._cardapio = []


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
    
    
    #def adicionar_bebida_no_cardapio(self, bebida):
    #    self._cardapio.append(bebida)

    
    #def adicionar_prato_no_cardapio(self, prato):
    #    self._cardapio.append(prato)
        
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            print('O item não é um prato ou bebida')
            return
        self._cardapio.append(item)


    @property
    def exibir_cardapio(self):
        print("Restaurante ", self._nome)
        for i, item in enumerate(self._cardapio, start=1):
            mensagem = f'{i} - {item} - R$ {item.preco}' 
            print(mensagem)