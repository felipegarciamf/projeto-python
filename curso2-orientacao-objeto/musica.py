class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
    def __str__(self):
        return self.nome


musica1 = Musica('The Scientist', 'Coldplay', '5:09')


print(musica1)
musicas = [vars(musica1)]

print(musicas)



class Teste:
    def __init__(self, teste):
        self.teste = teste
    def __srt__(self):
        return self.teste



teste = Teste('teste do sileira')


print(teste)
print(vars(teste))



def cadastro_musicao(nome, artista, duracao):
    musica = Musica(nome, artista, duracao)
    print(vars(musica))



## cadastro_musicao("joseph", "teste", "vai")