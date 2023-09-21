from conta.conta import Conta
from conta.contapoupanca import ContaPoupanca
from conta.contaespecial import ContaEspecial

class BancoList:
    def __init__(self):
        self.contas = []

    def cadastrar(self, conta: Conta):
        self.contas.append(conta)

    def cadastrarPoupanca(self, conta: ContaPoupanca):
        pass
    def cadastrarEspecial(self, conta: ContaEspecial):
        pass
