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
        if len(self.criancasPulando) < self.limeteMax and len(self.fila_de_espera) > 0:
            crianca = self.fila_de_espera[0]
            self.fila_de_espera.pop(0)
            self.criancasPulando.insert(0,crianca)
            self.conta += 2.50
            return True
        else:
            return False


    def sair(self):
        if len(self.criancasPulando) > 0:
            crianca = self.criancasPulando[0]
            self.criancasPulando.pop(0)
            self.fila_de_espera.append(crianca)
            return True
        return False


    def papaiChegou(self, nome):
        if self.criancasPulando:
            for crianca in self.criancasPulando:
                if crianca.nome == nome:
                    self.caixa += self.conta
                    self.conta = 0
                    return True
        elif self.fila_de_espera:
            for crianca in self.fila_de_espera:
                if crianca.nome == nome:
                    self.caixa += self.conta
                    self.conta = 0
                    self.fila_de_espera.remove(crianca)
                    return True
        return False


    def fechar(self):
        if self.criancasPulando:
            self.criancasPulando.clear()
            self.conta = None
        if self.fila_de_espera:
            self.fila_de_espera.clear()
            self.conta = None
        return -1