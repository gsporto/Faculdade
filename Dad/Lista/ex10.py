class no:
    def __init__(self):
        self.__inteiro = None
        self.__prox = None

    def getInteiro(self):
        return self.__inteiro

    def setInteiro(self, inteiro):
        self.__inteiro = inteiro

    def getProx(self):
        return self.__prox

    def setProx(self, prox):
        self.__prox = prox


class lista:
    def __init__(self):
        self.__ini = None
        self.__fim = None

    def push(self):
        temp = no()
        if temp is not None:
            temp.setInteiro(int(input('Numéro: ')))
            if self.__ini is None:
                self.__ini = self.__fim = temp
                return

            elif temp.getInteiro() <= self.__ini.getInteiro():
                temp.setProx(self.__ini)
                self.__ini = temp
                return

            elif temp.getInteiro() >= self.__fim.getInteiro():
                self.__fim.setProx(temp)
                self.__fim = temp
                return

            aux = self.__ini
            while True:
                if aux.getProx() is not None:
                    if aux.getProx().getInteiro() > temp.getInteiro():
                        temp.setProx(aux.getProx())
                        aux.setProx(temp)
                        return
                    else:
                        aux = aux.getProx()

    def pop_all(self):
        if self.__ini is None:
            print("lista Vazia!")
            return
        self.__ini = self.__fim = None
        print("Todos os itens da lista removidos!")

    def pop(self):
        if self.__fim is None:
            print("lista Vazia!")
            return
        num = int(input("Deseja excluir qual elemento? "))
        temp = self.__ini
        if temp.getInteiro() is num:
            self.__ini = self.__ini.getProx()
            if self.__ini is None:
                self.__fim = None
            return
        while temp.getProx() is not None:
            if temp.getProx().getInteiro() is num:
                temp.setProx(temp.getProx().getProx())
                if temp.getProx() is None:
                    self.__fim = temp
                break
            temp = temp.getProx()


    def print_all(self):
        if self.__ini is None:
            print("Lista Vazia!")
            return
        saida = ""
        soma = 0
        cont = 0
        par = ""
        impar = ""
        temp_no = self.__ini
        while temp_no is not None:
            cont += 1
            saida += "Valor: " + str(temp_no.getInteiro()) + "\n" ## mostra/concatena
            soma += temp_no.getInteiro()
            if temp_no.getInteiro() % 2:
                par += str(temp_no,getInteiro())
            else:
                impar += str(temp_no,getInteiro())
            temp_no = temp_no.getProx()
        print(saida + (soma/cont))

l = lista()
op = 0
while True:
    op = int(input(':'))
    if op is 1:
        l.push()
    elif op is 2:
        l.pop()
    elif op is 3:
        l.print_all()
    elif op is 4:
        l.pop_all()
    else:
        break
