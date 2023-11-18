from ....src.cliente.irh_service import IRHService
from ..base.funcionario import Funcionario
from ..base.professor import Professor
from ..base.sta import STA
from ..base.terceirizado import Terceirizado
from ....src.cliente.tipo import Tipo


class RHService(IRHService):


    def __init__(self):
        self.funcionarios = []
        self.salarioSTA = 0
        self.gratificacao = 0
        self.folhaDePagamento = 0
        self.terc_insalubre = 1500
        self.salario_terc = 1000

        # salarios dos profs:
        self.salProfs = {'A': 3000, 'B': 5000, 'C': 7000, 'D': 9000, 'E': 11000, 'terc_insal': 1500, 'terc': 1000}


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
                return False
            return False
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


    def solicitarDiaria(self, cpf: str):
        funcionario = self.obterFuncionario(cpf)
        if isinstance(funcionario, Professor):
            if funcionario.obter_diarias() < 3:
                funcionario.adicionar_diaria()
                return True
            return False
        elif isinstance(funcionario, STA):
            if funcionario.obter_diarias() < 1:
                funcionario.adicionar_diaria()
                return True
            return False
        elif isinstance(funcionario, Terceirizado):
            return False


    def partilharLucros(self, valor: float):
        if self.funcionarios:
            self.gratificacao = valor/len(self.funcionarios)
            return True


    def iniciarMes(self):
        self.salProfs = {'A': 3000, 'B': 5000, 'C': 7000, 'D': 9000, 'E': 11000, 'terc_insal': 1000, 'terc': 1500}
        self.salario_terc = 1000
        self.terc_insalubre = 1500
        self.diariaSTA = 0
        self.gratificacao = 0
        return True


    def calcularSalarioDoFuncionario(self, cpf: str):
        funcionario = self.obterFuncionario(cpf)
        if isinstance(funcionario, Professor):
            if funcionario.obter_diarias() > 0:
                salario = self.salProfs[funcionario.classe] + (funcionario.obter_diarias() * 100) + self.gratificacao
                return salario
            else:
                return self.salProfs[funcionario.classe] + self.gratificacao

        elif isinstance(funcionario, STA):
            if funcionario.obter_diarias() == 1:
                self.salario_sta = 1000 + (100 * funcionario.nivel) + 100 + self.gratificacao
                return self.salario_sta
            else:
                self.salario_sta = 1000 + (100 * funcionario.nivel) + self.gratificacao
                return self.salario_sta

        elif isinstance(funcionario, Terceirizado):
            if funcionario.insalubredade:
                return self.terc_insalubre + self.gratificacao
            else:
                return self.salario_terc + self.gratificacao

    def calcularFolhaDePagamento(self):
        self.folhaDePagamento = 0
        if self.funcionarios:
            professores = self.getFuncionariosPorCategorias(Tipo.PROF)
            stas = self.getFuncionariosPorCategorias(Tipo.STA)
            tercs = self.getFuncionariosPorCategorias(Tipo.TERC)

            for professor in professores:
                salario = self.calcularSalarioDoFuncionario(professor.cpf)
                self.folhaDePagamento += salario

            for sta in stas:
                salario = self.calcularSalarioDoFuncionario(sta.cpf)
                self.folhaDePagamento += salario

            for terc in tercs:
                salario = self.calcularSalarioDoFuncionario(terc.cpf)
                self.folhaDePagamento += salario

            return self.folhaDePagamento
        return 0