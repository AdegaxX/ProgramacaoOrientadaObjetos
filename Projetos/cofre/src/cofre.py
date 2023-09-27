from src.item import Item
from src.moeda import Moeda

class Cofre:

    def __init__(self, volumeMaximo: int):
        pass

    def getVolume(self):
        return -1

    def getVolumeMaximo(self):
        return -1

    def getVolumeRestante(self):
        return -1

    def add(self, item: Item):
        return False

    def add(self, moeda: Moeda):
        return False

    def obterItens(self):
        return "vazio"

    def obterMoedas(self):
        return -1

    def taInteiro(self):
        return False

    def quebrar(self):
        return False