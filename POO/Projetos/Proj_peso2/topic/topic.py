from POO.Projetos.Proj_peso2.topic.passageiro import Passageiro


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
        return self.qtdPrioritarios


    def getNumeroAssentosNormais(self):
        return self.vagasNormais


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
        if self.passPrioritario.count(None) == 0 and self.passNormais.count(None) == 0:
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


    def descer(self, nome:str):
        if self.passPrioritario.count(None) == 0:
            for passageiro in self.passPrioritario:
                if passageiro and passageiro.nome == nome:
                    self.passPrioritario.remove(passageiro)
                    self.vagas += 1
                    print(f'Passageiro {nome} desceu da cadeira preferencial.')
                    return True
            return False
        elif self.passNormais:
            for passageiro in self.passNormais:
                if passageiro and passageiro.nome == nome:
                    self.passNormais.remove(passageiro)
                    self.vagas += 1
                    print(f'Passageiro {nome} desceu da cadeira normal.')
                    return True
            return False
        else:
            print(f'Passageiro {nome} não encontrado!')
            return False


    def toString(self):
        for passageiro in self.passPrioritario:
            if passageiro != None:
                self.strings.insert(0, '@' + passageiro.nome)
            else:
                self.strings.append('@')
        for passageiro in self.passNormais:
            if passageiro != None:
                self.strings.append('=' + passageiro.nome)
            else:
                self.strings.append('=')
        lista = ' '.join(self.strings)
        return '[' + lista + ' ]'