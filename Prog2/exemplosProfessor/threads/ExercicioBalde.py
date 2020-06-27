import sys
import threading
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Janela(QWidget):
    __lb = None
    __le = None
    __pb = None
    __bt = None
    __gl = None

    __thread1 = None
    __thread2 = None

    __var_stop = 1
    __num = 0
    __anterior = -1

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Janela Principal')
        self.setFixedHeight(400)
        self.setFixedWidth(450)

        self.__lb = QLabel('Valor:')
        self.__le = QLineEdit('0')
        self.__pb = QProgressBar()
        self.__bt = QPushButton('Iniciar')
        self.__gl = QGridLayout()

        self.inicialize()

    def inicialize(self):
        self.__lb.setFixedWidth(30)
        self.__lb.setFixedHeight(30)

        self.__le.setEnabled(False)
        self.__le.setFixedWidth(70)
        self.__le.setFixedHeight(30)

        self.__pb.setOrientation(Qt.Vertical)
        self.__pb.setMaximumHeight(300)

        self.__bt.clicked.connect(self.bucket_controller)
        self.__bt.setFixedWidth(100)
        self.__bt.setFixedHeight(30)

        self.__gl.setAlignment(Qt.AlignHCenter)
        self.__gl.addWidget(self.__lb, 0, 0, Qt.AlignBottom)
        self.__gl.addWidget(self.__le, 0, 1, Qt.AlignBottom)
        self.__gl.addWidget(self.__pb, 0, 2, Qt.AlignHCenter)
        self.__gl.addWidget(self.__bt, 0, 3, Qt.AlignBottom)

        self.setLayout(self.__gl)
        self.show()

    def bucket_controller(self):
        if self.__var_stop == 1:
            self.__var_stop = 0
            self.action_thread()
            self.__bt.setText('Pausar')
        else:
            self.__var_stop = 1
            self.__thread1 = None
            self.__thread2 = None
            self.__bt.setText('Retomar')

    def action_thread(self):
        try:
            if 100 > self.__num > self.__anterior:
                self.__thread1 = threading.Thread(target=self.run_encher)
                self.__thread1.start()
            else:
                self.__thread2 = threading.Thread(target=self.run_esvaziar)
                self.__thread2.start()

        except Exception as ex:
            print('Erro na Thread')

    def run_encher(self):
        while self.__var_stop == 0 and self.__num < 100:
            self.__anterior = self.__num
            self.__num += 1
            self.__pb.setValue(self.__num + 2)
            self.__le.setText(str(self.__num))
            time.sleep(0.2)

        if self.__var_stop == 0:
            self.__thread1 = None
            self.action_thread()

    def run_esvaziar(self):
        while self.__var_stop == 0 and self.__num > 0:
            self.__anterior = self.__num
            self.__num -= 1
            self.__pb.setValue(self.__num - 2)
            self.__le.setText(str(self.__num))
            time.sleep(0.2)

        if self.__var_stop == 0:
            self.__anterior = -1
            self.__thread2 = None
            self.action_thread()


app = QApplication(sys.argv)

janela = Janela()

app.exec()