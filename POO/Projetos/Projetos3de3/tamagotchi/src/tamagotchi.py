class Tamagotchi:

    def __init__(self, energiaMax:int, saciedadeMax:int, limpezaMax:int, idadeMax:int ):
        self.energiaMax = energiaMax
        self.saciedadeMax = saciedadeMax
        self.limpezaMax = limpezaMax
        self.idadeMax = idadeMax
        self.energiaAtual = energiaMax
        self.saciedadeAtual = saciedadeMax
        self.limpezaAtual = limpezaMax
        self.idadeAtual = 0
        self.diamantes = 0
        self.EstaVivo = True


    def getEnergiaMax(self):
        return self.energiaMax

    def getSaciedadeMax(self):
        return self.saciedadeMax

    def getLimpezaMax(self):
        return self.limpezaMax

    def getIdadeMax(self):
        return self.idadeMax

    def getEnergiaAtual(self):
        return self.energiaAtual

    def getSaciedadeAtual(self):
        return self.saciedadeAtual

    def getLimpezaAtual(self):
        return self.saciedadeAtual

    def getIdadeAtual(self):
        return self.idadeAtual

    def getDiamantes(self):
        return self.diamantes

    def getEstaVivo(self):
        return True

    def brincar(self):
        if not self.EstaVivo:
            return False
        self.energiaAtual -= 2
        self.saciedadeAtual -= 1
        self.limpezaAtual -= 3
        self.diamantes += 1
        self.idadeAtual += 1
        return True

    def comer(self):
        if not self.EstaVivo:
            return False
        return True

    def dormir(self):
        if not self.EstaVivo:
            return False
        return True

    def banhar(self):
        if not self.EstaVivo:
            return False
        return True