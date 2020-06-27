import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Janela(QWidget):     ##Questão 1: Herda do Qt a classe de widgets
    __Lb_TituloItem=None
    __Lb_TituloQuant=None
    __Lb_TituloPreco=None
    __Lb_Total=None

    __Lb_Item=[]
    __LEd_Quant=[]
    __LEd_Preco=[]
    __LEd_Total=[]

    __LEd_TotalFinal=None
    __Bt_Calc=None

    def __init__(self, Str="Janela", x1=0, y1=0, dx=400, dy=190, cor="lightgray"):
        super().__init__()          ## Inicializa Super Classe
        self.setWindowTitle(Str)    ## Define Titulo
        self.setGeometry(x1, y1, dx, dy) ## Define Posição de inicio da tela e tamanho (Posição na tela Horizontal , Posição Vertical, Tamanho Altura, Tamanho Largura)

        self.setAutoFillBackground(True) ## Prenche fundo altomaticamente (Não Necessario but)
        p = self.palette() ## Instancia opção de cor
        p.setColor(self.backgroundRole(), QColor(cor)) ## Usa a instancia para definir a cor em p
        self.setPalette(p) ## Utiliza a instancia da cor no fundo 

        self.inicialize() ## Chama Inicialize

    def init_valores(self): ## Questão 3: Define os textos das labels em um array 
        self.__Lb_Item[0].setText('Arroz')
        self.__Lb_Item[1].setText('Açucar')
        self.__Lb_Item[2].setText('Batata')
        self.__Lb_Item[3].setText('Carne')
        self.__Lb_Item[4].setText('Feijão')

    def total_itens(self): ## Questão 4
        try:                                                ## Tenta rodar codigo se ouver erro vai para exception
            var_um = int(self.__LEd_Quant[0].text())        ## Pega Valor da 1° text quandidade
            var_dois = float(self.__LEd_Preco[0].text())    ## Pega Valor da 1° text Preço
            var_tres = var_um * var_dois                    ## Calculo Necessario
            self.__LEd_Total[0].setText(str(var_tres))      ## Define a caixa a 1° text total 

            var_um = int(self.__LEd_Quant[1].text())
            var_dois = float(self.__LEd_Preco[1].text())
            var_tres = var_um * var_dois
            self.__LEd_Total[1].setText(str(var_tres))

            var_um = int(self.__LEd_Quant[2].text())
            var_dois = float(self.__LEd_Preco[2].text())
            var_tres = var_um * var_dois
            self.__LEd_Total[2].setText(str(var_tres))

            var_um = int(self.__LEd_Quant[3].text())
            var_dois = float(self.__LEd_Preco[3].text())
            var_tres = var_um * var_dois
            self.__LEd_Total[3].setText(str(var_tres))

            var_um = int(self.__LEd_Quant[4].text())
            var_dois = float(self.__LEd_Preco[4].text())
            var_tres = var_um * var_dois
            self.__LEd_Total[4].setText(str(var_tres))
        except Exception as ex:                             ## Caso acha erro no try vem para cá
            print('Algo deu errado!')

    def total_final(self): ## Questão 5
        total_final = 0.0   ## Variavel auxiliar como zero
        try:            
            total_final += float(self.__LEd_Total[0].text())    ## Armazena o valor das totais
            total_final += float(self.__LEd_Total[1].text())
            total_final += float(self.__LEd_Total[2].text())    ## e soma elas
            total_final += float(self.__LEd_Total[3].text())
            total_final += float(self.__LEd_Total[4].text())
            self.__LEd_TotalFinal.setText(str(total_final))     ## Define a Text Total
        except Exception as ex:
            print('Algo deu errado!')

    def action_Bt_Calc(self):   ## Questão 6 Função chamada pelo botão
        self.total_itens()
        self.total_final()


    def inicialize(self): ## Inicialize
        Grid = QGridLayout() ## Define o uso de grids

        self.__Lb_TituloItem=QLabel(self, text="Item")          ## Cria Labels 
        self.__Lb_TituloQuant = QLabel(self, text="Quant.")
        self.__Lb_TituloPreco = QLabel(self, text="Preço")
        self.__Lb_Total = QLabel(self, text="Total")


        nl = 5
        for i in range(0, nl, 1):              ## Questão 7
            Lb = QLabel(self, text="")         ## Cria Label
            self.__Lb_Item.append(Lb)           ## Cria array destas labels
            self.LEd = QLineEdit()     ## Cria caixa de texto
            self.__LEd_Quant.append(LEd)        ## Cria Array de caixa de textos para quant
            LEd = QLineEdit(self, width=52)
            self.__LEd_Preco.append(LEd)
            LEd = QLineEdit(self, width=52)
            self.__LEd_Total.append(LEd)

        self.__Bt_Calc=QPushButton(self, text="Cálculo")   ## Cria Botão usando propriedade do qt
        self.__Bt_Calc.clicked.connect(self.action_Bt_Calc) ## .clicked é a ação do botão, e .connect qual função ele vai chamar
        self.__LEd_TotalFinal = QLineEdit(self, width=52)   ## Cria caixa de texto Total

        self.init_valores()         ## Chama Init valores para que a mesma preencha o array da questão 7

        Grid.addWidget(self.__Lb_TituloItem, 0, 0)  ## Define a posição no grig
        Grid.addWidget(self.__Lb_TituloQuant, 0, 1)
        Grid.addWidget(self.__Lb_TituloPreco, 0, 2)
        Grid.addWidget(self.__Lb_Total, 0, 3)

        nl = 5
        for i in range(0, nl, 1):       ## usa um for para posição das caixas de texto
            Grid.addWidget(self.__Lb_Item[i], i + 1, 0)     
            Grid.addWidget(self.__LEd_Quant[i], i + 1, 1)
            Grid.addWidget(self.__LEd_Preco[i], i + 1, 2)
            Grid.addWidget(self.__LEd_Total[i], i + 1, 3)

        Grid.addWidget(self.__Bt_Calc, 6, 1)        
        Grid.addWidget(self.__LEd_TotalFinal, 6, 2)

        self.setLayout(Grid) ## set o layout com os grids feitos  
        self.show() ## Exibe a Tela


## Questão 2
App=QApplication(sys.argv)
jan = Janela('Porto')
App.exec_()