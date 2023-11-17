from ....src.cliente.irh_service import IRHService
from ..base.funcionario import Funcionario
from ..base.professor import Professor
from ..base.sta import STA
from ..base.terceirizado import Terceirizado


class RHService(IRHService):


    def __init__(self):
        self.funcionarios = []
        self.salarioSTA = 0
        self.gratificacao = 0
        self.folhaDePagamento = 0
        self.terc_insalubre = 1500
        self.salario_terc = 1000

        # salarios dos profs:
        self.profA = 3000
        self.profB = 5000
        self.profC = 7000
        self.profD = 9000
        self.profE = 11000


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
        for cadastro in self.funcionarios:
            if cadastro.cpf == cpf:
                self.funcionarios.remove(cadastro)
                return True
        return False


    def obterFuncionario(self, cpf: str):
        for cadastro in self.funcionarios:
            if cadastro.cpf == cpf:
                return cadastro
        return None


    def getFuncionarios(self):
        return sorted(self.funcionarios, key=lambda funcionario: funcionario.nome)


    def getFuncionariosPorCategorias(self, tipo):
        if tipo == tipo.PROF:
            funcionarios_do_tipo = [funcionario for funcionario in self.funcionarios if isinstance(funcionario, Professor)]
        elif tipo == tipo.STA:
            funcionarios_do_tipo = [funcionario for funcionario in self.funcionarios if isinstance(funcionario, STA)]
        elif tipo == tipo.TERC:
            funcionarios_do_tipo = [funcionario for funcionario in self.funcionarios if isinstance(funcionario, Terceirizado)]
        else:
            return []
        funcionarios_do_tipo.sort(key=lambda x: x.nome)
        return funcionarios_do_tipo


    def getTotalFuncionarios(self):
        return len(self.funcionarios)


    def solicitarDiaria(self, cpf: str, professor: Professor):
        if self.obterFuncionario(cpf):
            func = self.obterFuncionario(cpf)
            if isinstance(func, Professor):
                diarias = func.obter_diarias()
                if diarias < 3:
                    if func.classe == 'A':
                        func.adicionar_diarias()
                        self.profA += 100
                        return True
                    if func.classe == 'B':
                        func.adicionar_diarias()
                        self.profB += 100
                        return True
                    if func.classe == 'C':
                        func.adicionar_diarias()
                        self.profC += 100
                        return True
                    if func.classe == 'D':
                        func.adicionar_diarias()
                        self.profD += 100
                        return True
                    if func.classe == 'E':
                        func.adicionar_diarias()
                        self.profE += 100
                        return True
            if isinstance(func, STA):
                diarias = func.obter_diarias()
                if diarias < 1:
                    func.adicionar_diarias()
                    self.salarioSTA += 100
            if isinstance(func, Terceirizado):
                return False


    def partilharLucros(self, valor: float):
        if self.funcionarios:
            self.gratif = valor/len(self.funcionarios)


    def iniciarMes(self):
        self.diariaProf = 0
        self.diariaSTA = 0
        self.gratificacao = 0


    def calcularSalarioDoFuncionario(self, cpf: str):
        func = self.obterFuncionario(cpf)
        if isinstance(func, Professor):
            if func.classe == 'A':
                self.folhaDePagamento += self.profA
                return self.profA
            if func.classe == 'B':
                self.folhaDePagamento += self.profB
                return self.profB
            if func.classe == 'C':
                self.folhaDePagamento += self.profC
                return self.profC
            if func.classe == 'D':
                self.folhaDePagamento += self.profD
                return self.profD
            if func.classe == 'E':
                self.folhaDePagamento += self.profE
                return self.profE

        elif isinstance(func, STA):
            self.salarioSTA += 1000 * (100 * func.nivel)
            return self.salarioSTA

        elif isinstance(func, Terceirizado):
            if func.insalubredade:
                self.folhaDePagamento += self.terc_insalubre
                return self.terc_insalubre
            else:
                self.folhaDePagamento += self.salario_terc
                return self.salario_terc


    def calcularFolhaDePagamento(self):
        return self.folhaDePagamento