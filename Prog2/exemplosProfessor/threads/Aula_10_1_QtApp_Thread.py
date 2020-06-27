import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import threading
import time

class meuThread:
    __Total = None
    __Delay=None
    __LEd = None
    __Thr = None

    def __init__(self, LEd_a):
        super().__init__()
        self.__LEd = LEd_a

    def iniciar(self, Total_a, Delay_a):
        try:
            if (self.__Thr is None):
                self.__Total = Total_a
                self.__Delay=Delay_a
                self.__Thr = threading.Thread(target=self.run)
                self.__Thr.start()
        except Exception as ex:
            print("Error: unable to start thread: %s\n" % (ex))

    def parar(self):
        try:
            self.__Total = 0
            self.__Thr = None
        except Exception as ex:
            print("Error: unable to start thread: %s\n" % (ex))

    def isRunning(self):
        if (self.__Thr is None):
            return(False)
        else:
            return(True)

    def run(self):
        count = 0
        while count < self.__Total:
            count += 1
            self.__LEd.setText("%d" % count)
            time.sleep(self.__Delay)


class Janela(QWidget):
    __LEd1 = None
    __LEd2 = None
    __LEd3 = None
    __Thr1 = None
    __Thr2 = None
    __Thr3 = None

    def __init__(self, Str="Janela", x1=0, y1=0, dx=640, dy=480, cor="ligthgray"):
        super().__init__()  ## Obrigatório
        self.setWindowTitle(Str)
        self.setGeometry(x1, y1, dx, dy)

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(cor))
        self.setPalette(p)

        self.inicialize()

    def action_Iniciar1(self):
        if (self.__Thr1.isRunning()):
            self.__Thr1.parar()
        else:
            self.__Thr1.iniciar(3000, 0.4)

    def action_Iniciar2(self):
        if (self.__Thr2.isRunning()):
            self.__Thr2.parar()
        else:
            self.__Thr2.iniciar(3000, 0.4)

    def action_Iniciar3(self):
        if (self.__Thr3.isRunning()):
            self.__Thr3.parar()
        else:
            self.__Thr3.iniciar(3000, 0.4)

    def inicialize(self):
        Grid = QGridLayout()

        self.__LEd1=QLineEdit(self, width=20)
        self.__LEd2=QLineEdit(self, width=20)
        self.__LEd3=QLineEdit(self, width=20)

        self.__Thr1 = meuThread(self.__LEd1)
        self.__Thr2 = meuThread(self.__LEd2)
        self.__Thr3 = meuThread(self.__LEd3)

        Bt1=QPushButton(self, text='Processo N.1')
        Bt2=QPushButton(self, text='Processo N.2')
        Bt3=QPushButton(self, text='Processo N.3')

        Bt1.clicked.connect(self.action_Iniciar1)
        Bt2.clicked.connect(self.action_Iniciar2)
        Bt3.clicked.connect(self.action_Iniciar3)

        Grid.addWidget(Bt1, 0, 0)
        Grid.addWidget(Bt2, 0, 1)
        Grid.addWidget(Bt3, 0, 2)

        Grid.addWidget(self.__LEd1, 1, 0)
        Grid.addWidget(self.__LEd2, 1, 1)
        Grid.addWidget(self.__LEd3, 1, 2)

        self.setLayout(Grid)
        self.show()


App=QApplication(sys.argv)

Jan1 = Janela("Minha janela", 400, 200, 540, 380, "orange")

App.exec_()
