import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Janela(QWidget):
    def __init__(self, Str="Janela", x1=0, y1=0, dx=640, dy=480, cor="lightgray"):
        super().__init__()  ## Obrigatório
        self.setWindowTitle(Str)
        self.setGeometry(x1, y1, dx, dy)

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(cor))
        self.setPalette(p)

        self.inicialize()

    def action_Bt1(self):
        self.Txt1.append("Botão 1:")

    def action_Bt2(self):
        self.Txt1.append("Botão 2:")

    def action_Bt3(self):
        self.Txt1.append("Botão 3:")

    def action_Bt4(self):
        self.Txt1.append("Botão 4:")

    def inicialize(self):
        Grid=QGridLayout()
        ## Grid.setColumnStretch(0, 1) ## Esticar somente o Txt1

        Bt1=QPushButton(self, text='Botão 1')
        Bt2=QPushButton(self, text='Botão 2')
        Bt3=QPushButton(self, text='Botão 3')
        Bt4=QPushButton(self, text='Botão 4')

        Bt1.clicked.connect(self.action_Bt1)
        Bt2.clicked.connect(self.action_Bt2)
        Bt3.clicked.connect(self.action_Bt3)
        Bt4.clicked.connect(self.action_Bt4)

        Bt1.setCursor(Qt.WaitCursor)

        self.Txt1 = QTextEdit(self, height=6, width=60)

        Grid.addWidget(Bt1, 0, 0)
        Grid.addWidget(Bt2, 0, 1)
        Grid.addWidget(Bt3, 0, 2)
        Grid.addWidget(Bt4, 0, 3)

        Grid.addWidget(self.Txt1, 1, 0, 1, 4)

        self.setLayout(Grid)
        self.show()

########################################################################################################################

App=QApplication(sys.argv)

Jan1=Janela("Minha janela", 400, 200, 540, 380, "orange")

App.exec_()
