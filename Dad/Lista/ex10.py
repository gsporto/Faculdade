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

    def qtElem(self):
        cont = 0
        temp_no = self.__ini
        while temp_no is not None:
            temp_no = temp_no.getProx()
            cont += 1
        return cont

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
        lista.print_all(self)

    def pop(self):
        if self.__fim is None:
            print("lista Vazia!")
            return
        lista.print_all(self)
        num = int(input("Deseja excluir qual elemento? "))
        temp = self.__ini
        if temp.getInteiro() is num:
            self.__ini = self.__ini.getProx()
            if self.__ini is None:
                self.__fim = None
            lista.print_all(self)
            return
        while temp.getProx() is not None:
            if temp.getProx().getInteiro() is num:
                temp.setProx(temp.getProx().getProx())
                if temp.getProx() is None:
                    self.__fim = temp
                break
            temp = temp.getProx()
        lista.print_all(self)

    def print_all(self):
        if self.__ini is None:
            print("Lista Vazia!")
            return
        saida = ""
        qt = lista.qtElem(self)
        if qt > 1:
            saida += "Imprimindo os " + str(qt) + " elementos da lista.\n"
        else:
            saida += "Imprimindo o elemento da lista.\n"
        temp_no = self.__ini
        while temp_no is not None:
            saida += "Valor: " + str(temp_no.getInteiro()) + "\n"
            temp_no = temp_no.getProx()
        print(saida)

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
