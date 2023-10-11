from ..src.item import Item
from ..src.moeda import Moeda

class Cofre:

    def __init__(self, volumeMaximo: int):
        self.volumeMaximo = volumeMaximo
        self.volume = 0
        self.volume_livre = volumeMaximo - self.volume
        self.quebrou = False
        self.itens = ''
        self.moedas = 0


    def getVolume(self):
        return self.volume


    def getVolumeMaximo(self):
        return self.volumeMaximo


    def getVolumeRestante(self):
        return self.volume_livre


    def addItem(self, item: Item):
        if self.volume == self.volumeMaximo:
            return False
        if self.quebrou == False:
            if item.volume <= self.volume_livre:
                self.volume += item.volume
                if self.itens:
                    self.itens += f', {item.descricao}'
                else:
                    self.itens += item.descricao
                self.volume_livre = self.volumeMaximo - self.volume
                return True
        else:
            return False


    def addMoeda(self, moeda: Moeda):
        if self.volume == self.volumeMaximo:
            return False
        if self.quebrou == False:
            if moeda.volume <= self.volume_livre:
                self.volume += moeda.volume
                self.moedas += moeda.valor
                self.volume_livre = self.volumeMaximo - self.volume
                return True
        else:
            return False


    def obterItens(self):
        if self.quebrou == True:
            if self.itens:
                return self.itens
            else:
                return "vazio"
        else:
            return None



    def obterMoedas(self):
        if self.quebrou == True:
            return self.moedas
        else:
            return -1

    def taInteiro(self):
        if self.quebrou == True:
            return False
        return True

    def quebrar(self):
        if self.quebrou == True:
            return False
        else:
            self.quebrou = True
            return True