from ..conta.conta import Conta
from ..conta.contapoupanca import ContaPoupanca
from ..conta.contaespecial import ContaEspecial


class BancoList:
    def __init__(self):
        self.conta = []

    def cadastrar(self, conta: Conta):
        self.conta.append(conta)

    def cadastrarPoupanca(self, conta: ContaPoupanca):
        self.conta.append(conta)
    def cadastrarEspecial(self, conta: ContaEspecial):
        self.conta.append(conta)
    def procurarConta(self, numero):
        for conta in self.conta:
            if conta.get_numero() == numero:
                return conta
            else:
                return None
