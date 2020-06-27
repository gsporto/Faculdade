import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import threading
import time

class ThreadSchlacht:
    __Total=None
    __LED=None
    __Thr=None
    def __init__(self, LED_a):
        super().__init__()
        self.__LED = LED_a

    def iniciar(self, Total_a):
        try:
            if self.__Thr is None:
                self.__Total = Total_a
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
    def run(self):
        i = 0
        while i < self.__Total:
            i += 1
            self.__LED.setText("%d" % (i))
            tempo = random.random()
            time.sleep(tempo)



class Janela(QWidget):
        __LED1=None
        __LED2 = None
        __LED3 = None
        __Bt_Abertura=None
        __Bt_Fechamento=None
        __Barraca1 = None
        __Barraca2 = None
        __Barraca3 = None
        def __init__(self, stri = "Janela",x1=0, y1=0, dx=640 ,dy=480, cor='green'):
            super().__init__()
            self.setWindowTitle(stri)
            self.setGeometry(x1, y1, dx, dy)
            self.setAutoFillBackground(True)
            p = self.palette()
            self.setPalette(p)
            self.inicialize()
        def action_abertura(self):
            self.__Barraca1.iniciar(3000)
            self.__Barraca2.iniciar(3000)
            self.__Barraca3.iniciar(3000)
        def action_fechamento(self):
            self.__Barraca1.parar()
            self.__Barraca2.parar()
            self.__Barraca3.parar()
        def inicialize(self):
            Grid = QGridLayout()
            self.__LED1 = QLineEdit(self, width=20)
            self.__LED2 = QLineEdit(self, width=20)
            self.__LED3 = QLineEdit(self, width=20)
            self.__Bt_Abertura = QPushButton(self, text='Abertura')
            self.__Bt_Fechamento = QPushButton(self, text='Fechamento')
            Grid.addWidget(self.__LED1, 0, 0, 1, 2)
            Grid.addWidget(self.__LED2, 1, 0, 1, 2)
            Grid.addWidget(self.__LED3, 2, 0, 1, 2)
            Grid.addWidget(self.__Bt_Abertura, 3, 0, 1, 1)
            Grid.addWidget(self.__Bt_Fechamento, 3, 1, 1, 1)
            self.__Barraca1 = ThreadSchlacht(self.__LED1)
            self.__Barraca2 = ThreadSchlacht(self.__LED2)
            self.__Barraca3 = ThreadSchlacht(self.__LED3)
            self.__Bt_Abertura.clicked.connect(self.action_abertura)
            self.__Bt_Fechamento.clicked.connect(self.action_fechamento)
            Grid.addWidget(self.__LED1, 0, 0, 1, 2)
            Grid.addWidget(self.__LED2, 1, 0, 1, 2)
            Grid.addWidget(self.__LED3, 2, 0, 1, 2)
            Grid.addWidget(self.__Bt_Abertura, 3, 0, 1, 1)
            Grid.addWidget(self.__Bt_Fechamento, 3, 1, 1, 1)
            self.setLayout(Grid)
            self.show()

App=QApplication(sys.argv)
Jan1 = Janela('Minha Janela ',400, 200, 540, 380, 'blue')

App.exec_()