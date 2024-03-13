class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao


musica1 = Musica('The Scientist', 'Coldplay', '5:09')


musicas = [vars(musica1)]

print(musicas)