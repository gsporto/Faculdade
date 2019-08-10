class node:
    def __init__(self):
        self.__ant = None
        self.__num = 0
        self.__prox = None

    def getAnt(self):
        return self.__ant

    def setAnt(self, ant):
        self.__ant = ant

    def getNum(self):
        return self.__num

    def setNum(self, num):
        self.__num = num

    def getProx(self):
        return self.__prox()

    def setProx(self, prox):
        self.__prox = prox


class lista:
    def __init__(self):
        self.__ini = None
        self.__fim = None

    def push(self):
        temp = node()
        if temp is not None:
            temp.setNum(int(input('Digite um Numero:')))
            #Primeiro nó da lista
            if self.__ini is None:
                self.__ini = self.__fim = temp
            #Inserção no inicio
            elif temp.getNum() <= self.__ini.getNum():
                temp.setProx(self.__ini)
                self.__ini.setAnt(temp)
                self.__ini = temp
            #Inserção no Final
            elif temp.getNum() >= self.__fim.getNum():
                temp.setAnt(self.__fim)
                self.__fim.setProx(temp)
                self.__fim = temp
            #Inserção no meio
            else:
                pant = self.__ini
                while True:
                    if temp.getNum() <= pant.getProx().getNum():
                        temp.setProx(pant.getProx)
                        temp.setAnt(pant)
                        pant.getProx().setAnt(temp)
                        pant.setProx(temp)
                        break
                    pant=pant.getProx()

    def printAll(self):
        temp_no = self.__fim
        st=''
        while temp_no is not None:
            st+= str(temp_no.getNum())
            temp_no = temp_no.getAnt()
        print(st)       

        def printall(self):
            if self.__ini is None:
                return 
             #temp = self.__fim tras pra frente
            temp = self.__ini
            saida= "lista: \n"
            while temp is not None:
                saida += str(temp.getnum()) + "\n"
                temp = temp.getprox()
                #temp=temp.getant tras pra frente 
            print(saida)                       

        def pop (self):
            if self.__ini is None:
                return 
            num=int(input("valor p excluir:"))
            if self.__ini is num:
                self.ini=self.__ini.getprox()
                if self.__ini is None:
                    self.__fim = None
                else:
                    self.__ini.seant(None)
                return
            temp = self.__ini
            while temp is not None:
                if temp.getprox().getnum() is num:
                    temp.setprox(temp.getprox().getprox())
                    if temp.getprox().setant is not None:
                        temp.getprox().setant(temp)
                    else:
                        self.__fim = temp
                temp = temp.getProx()

l = lista()

l.push()
l.push()
l.push()
l.push()

l.printAll()