import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import threading
import time
import datetime

class meuThread:
    __LEd = None
    __Thr = None
    __Running = None

    def __init__(self, LEd_a):
        super().__init__()
        self.__LEd = LEd_a

    def iniciar(self):
        try:
            if (self.__Thr is None):
                self.__Running = True
                self.__Thr = threading.Thread(target=self.run)
                self.__Thr.start()
        except Exception as ex:
            print("Error: unable to start thread: %s\n" % (ex))

    def parar(self):
        try:
            self.__Thr = None
            self.__Running = False
        except Exception as ex:
            print("Error: unable to start thread: %s\n" % (ex))

    def isRunning(self):
        if (self.__Thr is None):
            return(False)
        else:
            return(True)

    def run(self):
        while self.__Running:
            now = datetime.datetime.now()
            H = now.hour
            M = now.minute
            S = now.second
            self.__LEd.setText("%d : %d : %d" % (H,M,S))
            time.sleep(0.5)

########################################################################################################################
########################################################################################################################

class Janela(QWidget):
    __LEd1 = None
    __Thr1 = None

    def __init__(self, Str="Janela", x1=0, y1=0, dx=640, dy=480):
        super().__init__()  ## Obrigatório
        self.setWindowTitle(Str)
        self.setGeometry(x1, y1, dx, dy)

        self.inicialize()

    def action_Iniciar1(self):
        if (self.__Thr1.isRunning()):
            self.__Thr1.parar()
        else:
            self.__Thr1.iniciar()

    def inicialize(self):
        Grid = QGridLayout()

        self.__LEd1=QLineEdit(self, width=20)

        self.__Thr1 = meuThread(self.__LEd1)
        self.action_Iniciar1()

        Bt1=QPushButton(self, text='Parar')


        Bt1.clicked.connect(self.action_Iniciar1)


        Grid.addWidget(Bt1, 1, 0)

        Grid.addWidget(self.__LEd1, 0, 0)

        self.setLayout(Grid)
        self.show()

########################################################################################################################

App=QApplication(sys.argv)

Jan1 = Janela("Minha janela", 400, 200, 540, 380)

App.exec_()
