class Espiral:
    def __init__(self):
        self.nome = ' - '
        self.quantidade = 0
        self.preco = 0

    def getNomeDoProduto(self):
        return self.nome

    def setNomeDoProduto(self, nome):
        self.nome = nome
        return self.nome

    def getQuantidade(self):
        return self.quantidade


    def setQuantidade(self, quant):
        self.quantidade = quant
        return self.quantidade

    def getPreco(self):
        self.preco

    def setPreco(self, preco):
        self.preco = preco
        self.preco