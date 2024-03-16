class Pessoa:
    def __init__(self, nome, idade, profissao):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao

    def __str__(self):
        return f'{self._nome} ({self._idade} | {self._profissao})'
    
    def aniversario(self):
        self._idade += 1

    @property
    def saudacao(self):
        if self._profissao:
            return f'Olá {self._profissao}'
        else:
            return 'Olá'
    

pessoa1 = Pessoa('João', 30, 'Programador')

print(pessoa1.saudacao)
print(pessoa1)