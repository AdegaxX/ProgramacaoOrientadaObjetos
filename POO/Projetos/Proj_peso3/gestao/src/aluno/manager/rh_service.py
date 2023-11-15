from ....src.cliente.irh_service import IRHService
from ..base.funcionario import Funcionario
from ..base.professor import Professor
from ..base.sta import STA
from ..base.terceirizado import Terceirizado


class RHService(IRHService):


    def __init__(self):
        self.funcionarios = []


    def cadastrar(self, funcionario: Funcionario):
        if isinstance(funcionario, Professor):
            if 'A' <= funcionario.classe <= 'E':
                if funcionario.cpf not in [c.getCpf() for c in self.funcionarios]:
                    self.funcionarios.append(funcionario)
                    return True
        elif isinstance(funcionario, STA):
            if 1 <= funcionario.nivel <= 30:
                if funcionario.cpf not in [c.getCpf() for c in self.funcionarios]:
                    self.funcionarios.append(funcionario)
                    return True
        else:
            if funcionario.cpf not in [c.getCpf() for c in self.funcionarios]:
                self.funcionarios.append(funcionario)
                return True
        return False


    def remover(self, cpf: str):
        funcionario = self.obterFuncionario(cpf)
        if funcionario:
            self.funcionarios.remove(funcionario)
            return True
        return False


    def obterFuncionario(self, cpf: str):
        return next((f for f in self.funcionarios if f.cpf == cpf), None)


    def getFuncionarios(self):
        return sorted(self.funcionarios, key=lambda f: f.nome)


    def getFuncionariosPorCategorias(self, tipo):
        if tipo == tipo.PROF:
            funcionarios_do_tipo = [funcionario for funcionario in self.funcionarios if
                                    isinstance(funcionario, Professor)]
        elif tipo == tipo.STA:
            funcionarios_do_tipo = [funcionario for funcionario in self.funcionarios if isinstance(funcionario, STA)]

        elif tipo == tipo.TERC:
            funcionarios_do_tipo = [funcionario for funcionario in self.funcionarios if
                                    isinstance(funcionario, Terceirizado)]
        else:
            return []  # Retornar uma lista vazia se o tipo não for reconhecido

        funcionarios_do_tipo.sort(key=lambda x: x.nome)
        return funcionarios_do_tipo


    def getTotalFuncionarios(self):
        return len(self.funcionarios)

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
        funcionario = self.obterFuncionario(cpf)
        if funcionario:
            salario_base = funcionario.calcularFolhaDePagamento()
            diarias = 100 * funcionario.diarias
            salario_total = salario_base + diarias
            return salario_total
        else:
            return None


    def calcularFolhaDePagamento(self):
        for funcionario in self.funcionarios:
            salario_total = self.calcularSalarioDoFuncionario(funcionario.cpf)
            if salario_total is not None:
                return salario_total
            return False