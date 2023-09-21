from conta import Conta
from contaespecial import ContaEspecial

class TesteConta:
    if __name__ == '__main__':
        conta = Conta('31.345-x')
        conta.creditar(20)
        especial = ContaEspecial('31.567-x')
        conta.creditar(20)
        conta = especial
        conta.creditar(20)
        print(conta.get_bonus())
        print(especial.get_bonus())