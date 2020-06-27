import Pyro4

Joao = Pyro4.Proxy("PYRONAME:Servidor.Aluno") # get a Pyro proxy to the greeting object
print(Joao)
print("%s" % Joao.toString()) # call method normally
