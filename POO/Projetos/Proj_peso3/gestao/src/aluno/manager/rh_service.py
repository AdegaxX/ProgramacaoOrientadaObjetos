from ....src.cliente.irh_service import IRHService
from ..base.funcionario import Funcionario

class RHService(IRHService):


    def __init__(self):
        self.funcionarios = []


    def cadastrar(self, funcionario: Funcionario):
        if not any(f.cpf == funcionario.cpf for f in self.funcionarios):
            self.funcionarios.append(funcionario)
            return True
        return False


    def remover(self, cpf: str):
        funcionario = self.obterFuncionario(cpf)
        if funcionario:
            self.funcionarios.remove(funcionario)
        return False


    def obterFuncionario(self, cpf: str):
        return next((f for f in self.funcionarios if f.cpf == cpf), None)


    def getFuncionarios(self):
        return sorted(self.funcionarios, key=lambda f: f.nome)


    def getFuncionariosPorCategorias(self, tipo):
        return sorted([f for f in self.funcionarios if f.tipo == tipo], key=lambda f: f.nome)


    def getTotalFuncionarios(self):
        return self.funcionarios

    def solicitarDiaria(self, cpf: str):
        return False

    def partilharLucros(self, valor: float):
        num_funcionarios = len(self.funcionarios)
        if num_funcionarios > 0:
            valor_por_funcionario = valor / num_funcionarios
            for funcionario in self.funcionarios:
                funcionario.divisao_nos_lucros += valor_por_funcionario
                return True
        return False


    def iniciarMes(self):
        pass

    def calcularSalarioDoFuncionario(self, cpf: str):
        return None

    def calcularFolhaDePagamento(self):
        return 0