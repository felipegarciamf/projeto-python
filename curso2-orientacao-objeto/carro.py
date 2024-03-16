class Carro:

    carros = []

    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        Carro.carros.append(self)  
    def __str__(self):
        return f'{self.marca} | {self.modelo}'
    
    def listar_carros():
        for carro in Carro.carros:
            print(carro)

    
carro1 = Carro('fiat', 'uno', 2020, 'vermelho')
carro2 = Carro('chevrolet', 'saveiro', 2020, 'vermelho')

Carro.listar_carros()


