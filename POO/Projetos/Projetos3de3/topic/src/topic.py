from ..src.passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios):
        self.capacidade = capacidade
        self.qtdPrioritarios = qtdPrioritarios


    def getNumeroAssentosPrioritarios(self):
        if self.qtdPrioritarios > self.capacidade:
            return 'IllegalArgumentException'
        else:
            return self.qtdPrioritarios


    def getNumeroAssentosNormais(self):
        return self.capacidade
        print('\n')


    def getPassageiroAssentoNormal(self, lugar):
        return None


    def getPassageiroAssentoPrioritario(self, lugar):
        return None

    def getVagas(self):
        return -1

    def subir(self, passageiro: Passageiro):
        return False

    def descer(self, nome):
        return True