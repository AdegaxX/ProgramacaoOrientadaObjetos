class ContaImposto(Conta):
    def __init__(self, numero):
        super().__init__(numero)

    def debitar(self, valor):
        super().debitar(valor + (valor * 0.001))
