class Carro:

    def __init__(self):
        self.combustivel = 0
        self.quilometragem = 0
        self.passageiro = 0

    def getPassageiros(self):
        return self.passageiro

    def getCombustivel(self):
        return self.combustivel

    def getQuilometragem(self):
        return self.quilometragem

    def embarcar(self):
        if self.passageiro < 2:
            self.passageiro += 1
            return True
        else:
            return False

    def desembarcar(self):
        if self.passageiro > 0:
            self.passageiro -= 1
            return True
        else:
            return False

    def dirigir(self, distancia):
        if self.passageiro > 0 and self.combustivel > 0:
            if self.combustivel >= distancia:
                self.combustivel -= distancia
                self.quilometragem += distancia
                return True
            else:
                self.quilometragem += self.combustivel
                self.combustivel = 0
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
        return f"Passageiros: {self.passageiro}, Combustível: {self.combustivel} litros, Quilometragem: {self.quilometragem} km,"
