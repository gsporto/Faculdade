class node:
    def __init__(self):
        self.__nome = None
        self.__prox = None

    def setnome(self, nome):
        self.__nome = nome

    def getnome(self):
        return self.__nome

    def setprox(self, prox):
        self.__prox = prox

    def getprox(self):
        return self.__prox

class fila():
    def __init__(self):
        self.__ini = None
        self.__fim = None

    def push(self):
        temp = node()
        temp.setnome(input('Nome:'))
        if self.__fim is None:
            self.__fim = self.__ini = temp
        else:
            self.__fim.setprox(temp)
            self.__fim = temp

    def pop(self):
        if self.__ini is None:
            return
        else:
            self.__ini = self.__ini.getprox()

    def printall(self):
        aux = self.__ini
        st = ''
        if aux is None:
            return
        while aux is not None:
            st += aux.getnome()
            aux = aux.getprox()
        print(st)

f = fila()

f.push()
f.push()
f.push()

f.printall()

f.pop()
f.printall()