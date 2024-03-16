class ContaBancaria: 

    contas = []


    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)

    def __str__(self):
        return f'{self._titular} ({self._saldo} | {self._ativo})'
    

    @classmethod
    def listar_contas(cls):
        for conta in cls.contas:
            print(conta)

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'false'

    def ativarConta(self):
        self._ativo = not self._ativo
    

conta1 = ContaBancaria('João', 1000)
conta1.ativarConta()
conta2 = ContaBancaria('Maria', 2000)



ContaBancaria.listar_contas()