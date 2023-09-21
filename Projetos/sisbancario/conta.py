class Conta:
    def __init__(self, numero:int, saldo:float):
        self.limite = 100
        self.saldo = self.limite
        self.extrato = []

    def getNumero(self):
        return self.numero

    def getSaldo(self):
        return self.saldo

    def getLimite(self):
        return

    def sacar(self, valor:float):
        self.saldo -= valor
        print(f'- R${valor}')

    def depositar(self, valor:float):
        self.saldo += valor
        print(f'+ R${valor}')

    def transferir(self, destino, valor:float):
        return False

    def verExtrato(self):
        return self.extrato