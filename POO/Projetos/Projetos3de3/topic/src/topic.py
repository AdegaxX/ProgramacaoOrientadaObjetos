from ..src.passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios):
        self.capacidade = capacidade       # vagas totais
        self.qtdPrioritarios = qtdPrioritarios
        self.vagasNormais = capacidade - qtdPrioritarios
        self.passNormais = [None] * self.vagasNormais       # ex.: [None, None, None,...]
        self.passPrioritario = [None] * self.qtdPrioritarios
        self.strings = []
        self.vagas = capacidade     # vagas ainda não ocupadas


    def getNumeroAssentosPrioritarios(self):
        if self.qtdPrioritarios > self.capacidade:
            return 'IllegalArgumentException'
        else:
            return self.qtdPrioritarios


    def getNumeroAssentosNormais(self):
        return self.vagasNormais
        print('\n')


    def getPassageiroAssentoNormal(self, lugar):
        if lugar >= 0 and lugar < len(self.passNormais):
            return self.passNormais[lugar]
        else:
            return None


    def getPassageiroAssentoPrioritario(self, lugar):
        if self.passPrioritario.count(None) == 0:
            return self.passPrioritario[lugar]
        else:
            return None


    def getVagas(self):
        return self.vagas


    def subir(self, passageiro: Passageiro):
        if self.vagas > 0:
            return False
        if passageiro.idade >= 65:
            if None in self.passPrioritario:
                onde = self.passPrioritario.index(None)
                self.passPrioritario[onde] = passageiro
                self.vagas -= 1
                return True
            elif None in self.passNormais:
                onde = self.passNormais.index(None)
                self.passNormais[onde] = passageiro
                self.vagas -= 1
                return True
        elif passageiro.idade < 65:
            if None in self.passNormais:
                onde = self.passNormais.index(None)
                self.passNormais[onde] = passageiro
                self.vagas -= 1
                return True
            elif None in self.passPrioritario:
                onde = self.passPrioritario.index(None)
                self.passPrioritario[onde] = passageiro
                self.vagas -= 1
                return True
            return False
        return False


    def descer(self, nome):
        if self.passPrioritario.count(None) == 0:
            for i,passageiro in enumerate(self.passPrioritario):
                if passageiro.nome == nome:
                    self.passPrioritario.remove(passageiro)
                    self.vagas += 1
                    return True
            return False

        return True


    def toString(self):
        pass