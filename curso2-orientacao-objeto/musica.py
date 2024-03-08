class Musica:

    def init(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao



    nome = ''
    artista = ''
    duracao = ''

musica1 = Musica()
musica1.nome = 'The Scientist'
musica1.artista = 'Coldplay'
musica1.duracao = '5:09'

musica2 = Musica()
musica2.nome = 'Yellow'
musica2.artista = 'Coldplay'
musica2.duracao = '4:29'

musica3 = Musica()
musica3.nome = 'Fix You'
musica3.artista = 'Coldplay'
musica3.duracao = '4:55'


musicas = [vars(musica1), vars(musica2), vars(musica3)]

print(musicas)