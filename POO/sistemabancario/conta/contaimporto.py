from classabstrata import ContaAbstrata


class ContaImposto(ContaAbstrata):
    def __init__(self, numero):
        super().__init__(numero)

    def debitar(self, valor):
        self.__saldo = self.__saldo - (valor + (valor * 0.001))