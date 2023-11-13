from ....src.aluno.base.funcionario import Funcionario


class STA(Funcionario):

    def __init__(self, cpf: str, nome: str, nivel: int):
        super().__init__(cpf, nome, "STA")
        self.nivel = nivel
        self.salario_base = self.calcular_salario_base()

    def calcular_salario_base(self):
        return 1000 + 100 * self.nivel

    def calcular_diarias(self):
        return min(1, self.diarias) * 100