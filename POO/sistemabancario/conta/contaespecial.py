from conta import Conta


class ContaEspecial(Conta):
    def __init__(self, numero):
        super().__init__(numero)
        self.__bonus = 0

    def renderBonus(self):
        super().creditar(self.__bonus)
        self.__bonus = 0

    def creditar(self, valor):
        self.__bonus = self.__bonus + (valor * 0.01)
        super().creditar(valor)

    # def get_bonus(self):
    #    return self.__bonus
