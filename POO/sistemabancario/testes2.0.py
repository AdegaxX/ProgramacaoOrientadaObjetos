from POO.sistemabancario.conta.contapoupanca import ContaPoupanca
from conta import Conta

class CriarPoupanca:
    if __name__ == '__main__':
        opcao = int(input('Escolha: [1] Conta e [2] Poupanca: '))
        if opcao == 1:
            conta = Conta('21.342-7')
        else:
            conta = ContaPoupanca('21.342-7')

        conta.creditar(500.87)
        conta.debitar(45.00)

        if isinstance(conta, ContaPoupanca):
            conta.render_juros(0.1)
            print(f'Saldo com juros: {conta.get_saldo()}')