class Carro:

    def __init__(self):
        self.combustivel = 0    # Inicia as 'variáveis'
        self.passageiros = 0
        self.quilometragem = 0



    def getPassageiros(self):
        return self.passageiros


    def getCombustivel(self):
        return self.combustivel


    def getQuilometragem(self):
        return self.quilometragem


    def embarcar(self):
        if self.passageiros < 2:    # Para embarcar deve existir, ao menos, um lugar vago.
            self.passageiros += 1   # add um novo passageiro
            return True
        else:
            return False



    def desembarcar(self):
        if self.passageiros > 0:    # Para desembarcar deve haver ao menos 1 passageiro
            self.passageiros -= 1   # tira um passageiro
            return True
        else:
            return False



    def dirigir(self, distancia):
        if self.passageiros > 0 and self.combustivel > 0:   # se possuir algum passageiro e tiver combustível:
            if distancia <= self.combustivel:       # se a distância for menor ou igual ao combustível:
                self.quilometragem += distancia     # km aumenta
                self.combustivel -= distancia       # distância diminui
                return True
            else:
                self.quilometragem += self.combustivel
                self.combustivel = 0        # restaura o combustível
                return False



    def abastecer(self, quantidade):
        if quantidade > 0:
            if self.combustivel + quantidade <= 100:
                self.combustivel += quantidade
            else:
                self.combustivel = 100
            return True
        else:
            return False



        def __str__(self):
            return f"Passageiros: {self.passageiros}, Combustível: {self.combustivel} litros, Quilometragem: {self.quilometragem} km"

