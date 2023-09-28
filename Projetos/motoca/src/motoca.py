from ..src.pessoa import Pessoa


class Motoca:

    def __init__(self, potencia: int):
        pass

    def getPessoa(self):
        return None

    def getTempo(self):
        return -1

    def getPotencia(self):
        return -1

    def subir(self, pessoa: Pessoa):
        return False

    def descer(self):
        return False

    def colocarTempo(self, tempo: int):
        return False

    def dirigir(self, tempo: int):
        return True

    def buzinar(self):
        return None