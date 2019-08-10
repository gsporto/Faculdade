# Construa um programa que insere
# nomes em uma fila circular.


class node:
    def __init__(self):
        self.valor = None
        self.prox = None

    def setValor(self, valor=None):
        self.valor = valor

    def getValor(self):
        return self.valor

    def setProx(self, prox):
        self.prox = prox

    def getProx(self):
        return self.prox

