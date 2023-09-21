from POO.sistemabancario.conta.contapoupanca import ContaPoupanca
from conta import Conta

class CriarPoupanca:
    if __name__ == '__main__':
        conta = Conta('21.342-7')
        print(type(conta))
        conta = ContaPoupanca('21.342-7')
        print(type(conta))