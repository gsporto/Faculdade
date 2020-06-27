import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Janela(QWidget):
    __Lb1 = None
    __Lb2 = None
    __Lb3 = None
    def __init__(self, Str="Janela", x1=0, y1=0, dx=640, dy=480, cor="lightgray"):
        super().__init__() ## Obrigatório
        self.setWindowTitle(Str)
        self.setGeometry(x1, y1, dx, dy)

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(cor))
        self.setPalette(p)

        self.inicialize()

    def inicialize(self):
        Grid=QGridLayout()
        Grid.setColumnStretch(1, 4)
        Grid.setColumnStretch(2, 4)

        self.__Lb1=QLabel(self, text="First Name")
        self.__Lb2=QLabel(self, text="Last Name")
        self.__Lb3=QLabel(self, text="Text área")

        p1 = self.palette()
        p1.setColor(self.backgroundRole(), Qt.yellow)

        self.__Lb1.setAutoFillBackground(True)
        self.__Lb1.setPalette(p1)

        self.__Lb2.setAutoFillBackground(True)
        self.__Lb2.setPalette(p1)

        self.__Lb3.setAutoFillBackground(True)
        self.__Lb3.setPalette(p1)

        Et1=QLineEdit(self, width=52)
        Et2=QLineEdit(self, width=52)

        Txt1=QTextEdit(self, height=8, width=40)

        Bt1=QPushButton(self, text='Botão 1')
        Bt2=QPushButton(self, text='Botão 2')

        Grid.addWidget(self.__Lb1, 0, 0)
        Grid.addWidget(self.__Lb2, 1, 0)
        Grid.addWidget(self.__Lb3, 2, 0)

        Grid.addWidget(Et1, 0, 1, 1, 2)
        Grid.addWidget(Et2, 1, 1, 1, 2)
        Grid.addWidget(Txt1, 2, 1, 1, 2)

        Grid.addWidget(Bt1, 3, 1)
        Grid.addWidget(Bt2, 3, 2)

        self.setLayout(Grid)
        self.show()

########################################################################################################################

App=QApplication(sys.argv)

Jan1=Janela("Minha janela", 400, 200, 540, 380, "cyan")

App.exec_()
