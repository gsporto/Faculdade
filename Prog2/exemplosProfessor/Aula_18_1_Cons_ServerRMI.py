import Pyro4

@Pyro4.expose
class Aluno(object):
    __Nome=None
    __Cidade=None
    __Idade=None

    def __init__(self,nome,cidade,idade):
        self.__Nome=nome
        self.__Cidade=cidade
        self.__Idade=idade

    def Leitura(self):
        self.__Nome=input("Digite o nome: ")
        self.__Cidade=input("Digite a cidade: ")
        self.__Idade=int(input("Digite a idade: "))

    def toString(self):
        Str=""
        Str=Str+"Nome = %s\nCidade = %s\nIdade = %d\n" % (self.__Nome, self.__Cidade, self.__Idade)
        return(Str)

################################################################################

def main():
	daemon = Pyro4.Daemon() # make a Pyro daemon 
	nameServ=Pyro4.locateNS() # find the name server
	alu=Aluno("Joao","São Bento do Sul",19)
	## alu.Leitura()
	uri = daemon.register(alu) # registra o Aluno como um objeto Pyro
	nameServ.register("Servidor.Aluno", uri) # register the object with a name in the name, server

	print("Servidor =", nameServ, " Ok.") # print the uri so we can use it in the client, →later 
	daemon.requestLoop() # start the event loop of the server to wait

if __name__=="__main__":
    main()
