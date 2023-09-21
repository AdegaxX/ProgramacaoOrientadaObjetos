from abc import ABC, abstractmethod


class ContaAbstrata(ABC):
    def __init__(self, numero):
        self.__numero = numero
        self.__saldo = 0

    def creditar(self, valor):
        self.__saldo = self.__saldo + valor

    @property
    @abstractmethod
    def debitar(self, valor):
        pass

    def get_numero(self):
        return self.__numero

    def set_numero(self,numero):
        self.__numero = numero

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo