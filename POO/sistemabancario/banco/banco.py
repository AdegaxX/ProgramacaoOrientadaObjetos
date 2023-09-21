from conta import Conta

class Banco:
    def __init__(self):
        self.contas = []

    def cadastrar(self, conta: Conta):
        self.contas.append(conta)

    def procurar_conta(self, numero):

        for conta in self.contas:
            if conta.get_numero() == numero:
                return conta
            else:
                return None


    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            print('Conta inexistente!')


    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print('Conta inexistente!')

    def saldo(self, numero):
        # Procurar se a conta existe:
        conta = self.procurar_conta(numero)
        if conta:   # Se existir, irá mostrar o saldo
            return conta.get_saldo()
        else:
            print('Conta não encontrada!')

    def transferir(self, origem, destino, valor):
        # Verificar se as duas contas existem:
        conta_origem = self.procurar_conta(origem)
        conta_destino = self.procurar_conta(destino)

        if conta_origem and conta_destino:  # Testa se as duas contas existem para realizar as transações
            if conta_origem.get_saldo() >= valor:   # Testa se o valor da tranf está na conta
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
                print('Transação realizada com sucesso!')
            else:
                print('Saldo insuficiente!')
        else:
            print('Conta inexistente!')