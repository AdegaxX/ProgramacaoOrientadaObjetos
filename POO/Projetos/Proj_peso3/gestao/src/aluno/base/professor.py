from ....src.aluno.base.funcionario import Funcionario


class Professor(Funcionario):

    def __init__(self, cpf: str, nome: str, classe: str):
        super().__init__(cpf, nome, 'Professor')
        self.classe = classe
        self.salario_base = self.calcular_salario_base()

    def calcular_salario_base(self):
        classes = {"A":3000, "B":5000, "C":7000, "D":9000, "E":11000}
        return classes.get(self.classe, 0)

    def calcular_diarias(self):
        return min(3, self.diarias) * 100