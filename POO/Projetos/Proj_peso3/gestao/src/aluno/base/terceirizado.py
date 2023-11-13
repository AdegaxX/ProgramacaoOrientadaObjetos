from ....src.aluno.base.funcionario import Funcionario


class Terceirizado(Funcionario):

    def __init__(self, cpf: str, nome: str, insalubredade=False):
        super().__init__(cpf, nome, "Terceirizado")
        self.salario_base = 1000
        self.insalubredade = insalubredade

    def calcular_diarias(self):
        return 0 if self.insalubredade else min(1, self.diarias) * 100