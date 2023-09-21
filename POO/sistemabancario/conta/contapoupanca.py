from conta import Conta
from banco import Banco

class ContaPoupanca:
    def __init__(self, numero):
        super().__init__(numero)

    def render_juros(self, taxa):
        self.creditar(self.get_saldo() * taxa)