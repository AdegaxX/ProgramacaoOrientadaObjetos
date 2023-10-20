from ..conta.conta import Conta
from ..conta.contapoupanca import ContaPoupanca
from ..conta.contaespecial import ContaEspecial
from ..conta.exceptionSI import SIException
from ..conta.exceptionCI import CIException


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


    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            conta = None


    def debitar(self, numero, valor):
        try:
            conta = self.procurarConta(numero)
            conta.debitar(valor)

        except CIException(numero) as errorci:
            print(errorci)

        except SIException(conta.get_saldo(), conta.get_numero()) as errorsi:
            print(errorsi)


    def saldo(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            conta.get_saldo()
        else:
            conta = None


    def transferir(self, origem, destino, valor):
        conta0 = self.procurar_conta(origem)
        conta1 = self.procurar_conta(destino)
        saldoso = Conta.get_saldo(origem)
        if saldoso > valor:
            if conta0 and conta1:
                conta0.debitar(valor)
                conta1.creditar(valor)
            else:
                conta = None
        else:
            print('sem saldo')


    def render_juros(self, numero, taxa=0.01):
        conta = self.procurar_conta(numero)
        if conta:
            if isinstance(conta, ContaPoupanca):
                conta.render_juros(taxa)
            else:
                print('Operação Indisponível')
        else:
            conta = None


        def render_bonus(self, numero, bonus=0.01):
            conta = self.procurar_conta(numero)
            if conta:
                if isinstance(conta, ContaEspecial):
                    conta.render_bonus()
                else:
                    print('Operação Indisponível')
            else:
                conta = None