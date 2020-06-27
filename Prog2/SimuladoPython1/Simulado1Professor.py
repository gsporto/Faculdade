import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Janela(QWidget):
    __Lb_TituloItem = None
    __Lb_TituloQuant = None
    __Lb_TituloPreco = None
    __Lb_Total = None
    __Lb_Item = []
    __LEd_Quant = []
    __LEd_Preco = []
    __LEd_Total = []

    __LEd_TotalFinal = None
    __Bt_Calc = None


    def __init__(self, Str="Janela", x1=0, y1=0, dx=640, dy=480, cor="lightgray"):
        super().__init__()  ## Obrigatório
        self.setWindowTitle(Str)
        self.setGeometry(x1, y1, dx, dy)
        # Set window background color
        #self.setAutoFillBackground(True)
        #p = self.palette()
        #p.setColor(self.backgroundRole(), QColor(cor))
       # self.setPalette(p)
        self.inicialize()

    def total_itens(self):
        try:
            for i in range(0, 5, 1):
                quant = int(self.__LEd_Quant[i].text())
                preco = float(self.__LEd_Preco[i].text())
                total = quant * preco
                self.__LEd_Total[i].setText("%s" % total)
        except ValueError as ve:
            QMessageBox.about(self, "Janela de Erro #1", "Voce deve digitar valores numéricos")
        except Exception as ex:
            QMessageBox.about(self, "Janela de Erro #2", "Erro desconhecido")

    def total_final(self):
        print("zzzzzzzzzzzzzzz")

    def action_Bt_Calc(self):
        self.total_itens()
        self.total_final()

    def init_valores(self):
        self.__Lb_Item[0].setText('Arroz')
        self.__Lb_Item[1].setText('Açucar')
        self.__Lb_Item[2].setText('Batata')
        self.__Lb_Item[3].setText('Carne')
        self.__Lb_Item[4].setText('Feijão')

        self.__LEd_Quant[0].setText('1')
        self.__LEd_Quant[1].setText('3')
        self.__LEd_Quant[2].setText('6')
        self.__LEd_Quant[3].setText('2')
        self.__LEd_Quant[4].setText('4')

        self.__LEd_Preco[0].setText('3.5')
        self.__LEd_Preco[1].setText('2.5')
        self.__LEd_Preco[2].setText('1.89')
        self.__LEd_Preco[3].setText('18.2')
        self.__LEd_Preco[4].setText('2.4')

    def inicialize(self):
        Grid = QGridLayout()

        p1 = self.palette()
        p1.setColor(self.backgroundRole(), QColor("yellow"))

        self.__Lb_TituloItem=QLabel(self, text="Item")
        self.__Lb_TituloQuant = QLabel(self, text="Quant.")
        self.__Lb_TituloPreco = QLabel(self, text="Preço")
        self.__Lb_Total = QLabel(self, text="Total")


        nl = 5
        for i in range(0, nl, 1):
            Lb = QLabel(self, text="")
            self.__Lb_Item.append(Lb)
            LEd = QLineEdit(self, width=52)
            self.__LEd_Quant.append(LEd)
            LEd = QLineEdit(self, width=52)
            self.__LEd_Preco.append(LEd)
            LEd = QLineEdit(self, width=52)
            self.__LEd_Total.append(LEd)

        self.__Bt_Calc=QPushButton(self, text="Cálculo")
        self.__Bt_Calc.clicked.connect(self.action_Bt_Calc)
        self.__LEd_TotalFinal = QLineEdit(self, width=52)

        self.init_valores()

        Grid.addWidget(self.__Lb_TituloItem, 0, 0)
        Grid.addWidget(self.__Lb_TituloQuant, 0, 1)
        Grid.addWidget(self.__Lb_TituloPreco, 0, 2)
        Grid.addWidget(self.__Lb_Total, 0, 3)

        nl = 5
        for i in range(0, nl, 1):
            Grid.addWidget(self.__Lb_Item[i], i + 1, 0)
            Grid.addWidget(self.__LEd_Quant[i], i + 1, 1)
            Grid.addWidget(self.__LEd_Preco[i], i + 1, 2)
            Grid.addWidget(self.__LEd_Total[i], i + 1, 3)

        Grid.addWidget(self.__Bt_Calc, 6, 1)
        Grid.addWidget(self.__LEd_TotalFinal, 6, 2)

        self.setLayout(Grid)
        self.show()

###################################################################################################

App=QApplication(sys.argv)

Jan1=Janela("Minha janela", 400, 200, 480, 200, "orange")

App.exec_()

