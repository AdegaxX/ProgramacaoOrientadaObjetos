class Debinha:
    def __init__(self, lindeza, tamanho, message = 'A debinha é muito pequenininha'):
        self.beleza = lindeza
        self.tamanho = tamanho
        self.message = message


    def getBeleza(self):
        return self.beleza

    def getTamanho(self):
        return self.tamanho


    def getMessagem(self):
        return self.message


    def descricao(self):
        return f''