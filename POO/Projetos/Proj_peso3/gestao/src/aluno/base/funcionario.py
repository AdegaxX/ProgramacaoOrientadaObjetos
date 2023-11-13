class Funcionario:

    def __init__(self, cpf, nome, cargo):
        self.cpf = cpf
        self.nome = nome
        self.cargo = cargo
        self.salario_base = 0
        self.divisao_nos_lucros = 0
        self.diarias = 0


    def getNome(self) -> str:
        return self.nome

    def getCpf(self) -> str:
        return self.cpf

    def getSalario(self) -> float:
        return self.salario