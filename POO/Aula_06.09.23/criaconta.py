from conta import Conta

class CriarConta:
    if __name__ == '__main__':
        conta = Conta('21.342-7')
        conta.creditar(700.87)
        #conta.debitar(60.00)
        print(conta.get_saldo())
        print(conta.get_numero())
