from ..src.crianca import Crianca
class PulaPula:

    def __init__(self, limiteMax):
        self.limeteMax = limiteMax

        self.fila_de_espera = []
        self.criancasPulando = []

        self.conta = 0
        self.caixa = 0


    def getFilaDeEspera(self):
        return self.fila_de_espera

    def getCriancasPulando(self):
        return self.criancasPulando

    def getLimiteMax(self):
        return self.limeteMax

    def getCaixa(self):
        return self.caixa

    def getConta(self, nome):
        for crianca in self.criancasPulando:
            if crianca.nome == nome:
                return self.conta

    def entrarNaFila(self, crianca: Crianca):
        if self.fila_de_espera:
            if self.criancasPulando:
                for crianca in self.criancasPulando:
                    if crianca.nome != crianca.nome:
                        self.fila_de_espera.append(crianca)
                        return True
                    return False
            else:
                self.fila_de_espera.append(crianca)
        else:
            self.fila_de_espera.insert(0, crianca)
            return True


    def entrar(self):
          
        return True

    def sair(self):
        return True

    def papaiChegou(self, nome):
        return False

    def fechar(self):
        return -1