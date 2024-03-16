class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} | {self.artista}'



def cadastro_musicao(nome, artista, duracao):
    musica = Musica(nome, artista, duracao)
    print(musica)

cadastro_musicao("joseph", "teste", "vai")