import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Janela():
    def __init__(self, Master, Str="Janela", x1=0, y1=0, dx=640, dy=480, cor="lightgray"):
        self.Master=Master
        self.Master.setWindowTitle(Str)
        self.Master.setGeometry(x1, y1, dx, dy)

        # Set window background color
        self.Master.setAutoFillBackground(True)
        p = self.Master.palette()
        p.setColor(self.Master.backgroundRole(), QColor(cor))
        self.Master.setPalette(p)

        self.inicialize(self.Master)

    def inicialize(self, Parent):
        Grid=QGridLayout()
        Grid.setColumnStretch(1, 4)
        Grid.setColumnStretch(2, 4)

        Lb1=QLabel(Parent, text="First Name")
        Lb2=QLabel(Parent, text="Last Name")
        Lb3=QLabel(Parent, text="Text área")

        p1 = Parent.palette()
        p1.setColor(Parent.backgroundRole(), Qt.yellow)

        Lb1.setAutoFillBackground(True)
        Lb1.setPalette(p1)

        Lb2.setAutoFillBackground(True)
        Lb2.setPalette(p1)

        Lb3.setAutoFillBackground(True)
        Lb3.setPalette(p1)

        Et1=QLineEdit(Parent, width=52)
        Et2=QLineEdit(Parent, width=52)

        Txt1=QTextEdit(Parent, height=8, width=40)

        Bt1=QPushButton(Parent, text='Botão 1')
        Bt2=QPushButton(Parent, text='Botão 2')

        Grid.addWidget(Lb1, 0, 0)
        Grid.addWidget(Lb2, 1, 0)
        Grid.addWidget(Lb3, 2, 0)

        Grid.addWidget(Et1, 0, 1, 1, 2)
        Grid.addWidget(Et2, 1, 1, 1, 2)
        Grid.addWidget(Txt1, 2, 1, 1, 2)

        Grid.addWidget(Bt1, 3, 1)
        Grid.addWidget(Bt2, 3, 2)

        Parent.setLayout(Grid)
        Parent.show()

########################################################################################################################

App=QApplication(sys.argv)

Root=QWidget()
Jan1=Janela(Root, "Minha janela", 400, 200, 540, 380, "orange")

App.exec_()
