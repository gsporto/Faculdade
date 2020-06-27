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

    def show_mensagem_erro(self, title="Titulo da janela", texto="Ocorreu um erro", informacao="Informação adicional", detalhes="Informação detalhada"):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(texto)
        msg.setInformativeText(informacao)
        msg.setDetailedText(detalhes)
        msg.setSizeGripEnabled(True) ## Nao funciona
        msg.setBaseSize(320, 240) ## Nao funciona
        msg.setMaximumSize(320, 240) ## Nao funciona
        msg.exec_()

    def action_Bt_Calc(self):
        try:
            num=int(self.LEd_NumPrest.text())
            val=float(self.LEd_ValPrest.text())
            total=num*val
            self.LEd_Total.setText("%4.2f" % total)
        except ValueError as ve:
            ## Primeira solução
            QMessageBox.about(None, "Janela de Erro #1", "Voce deve digitar valores numéricos")
            ## Segunda solução
            QMessageBox.about(self, "Janela de Erro #2", "Voce deve digitar valores numéricos")
            ## Terceira solução
            self.show_mensagem_erro("Janela de Erro #3", "Erro de digitação___________\t___________", "Voce deve digitar valores numéricos",
                                    "Erro1: Voce deve digitar valores numéricos: \n\n%s" % ve)
            print("Erro1: Voce deve digitar valores numéricos: \n\n%s" % ve)
        except Exception as ex:
            self.show_mensagem_erro("Janela de Erro", "Erro fatal", "Verifique nos detalhes o que ocorreu",
                                    "Erro2: Erro inexperado: \n\n%s" % ex)
            print("Erro2: Erro inexperado: \n\n%s" % ex)

    def inicialize(self):
        Grid=QGridLayout()
        ## Grid.setColumnStretch(1, 4)
        ## Grid.setColumnStretch(2, 4)

        Lb_Cliente=QLabel(self, text="Cliente=")
        Lb_Niver=QLabel(self, text="Niver=")
        Lb_NumPrest=QLabel(self, text="NumPrest=")
        Lb_ValPrest= QLabel(self, text="ValPrest=")
        Lb_Total = QLabel(self, text="Total=")

        Lb_Cliente.setAlignment(Qt.AlignRight)
        Lb_Niver.setAlignment(Qt.AlignRight)
        Lb_NumPrest.setAlignment(Qt.AlignRight)
        Lb_ValPrest.setAlignment(Qt.AlignRight)
        Lb_Total.setAlignment(Qt.AlignRight)

        p1 = self.palette()
        p1.setColor(self.backgroundRole(), Qt.yellow)

        Lb_Cliente.setAutoFillBackground(True)
        Lb_Cliente.setPalette(p1)

        Lb_Niver.setAutoFillBackground(True)
        Lb_Niver.setPalette(p1)

        Lb_NumPrest.setAutoFillBackground(True)
        Lb_NumPrest.setPalette(p1)

        Lb_ValPrest.setAutoFillBackground(True)
        Lb_ValPrest.setPalette(p1)

        Lb_Total.setAutoFillBackground(True)
        Lb_Total.setPalette(p1)

        LEd_Cliente=QLineEdit(self, width=52)
        LEd_Niver=QLineEdit(self, width=52)
        self.LEd_NumPrest = QLineEdit(self, width=52)
        self.LEd_ValPrest = QLineEdit(self, width=52)
        self.LEd_Total = QLineEdit(self, width=52)

        Bt_Calc=QPushButton(self, text='Calcular')
        Bt_Calc.clicked.connect(self.action_Bt_Calc)

        Grid.addWidget(Lb_Cliente, 0, 0)
        Grid.addWidget(Lb_Niver, 1, 0)
        Grid.addWidget(Lb_NumPrest, 2, 0)
        Grid.addWidget(Lb_ValPrest, 3, 0)
        Grid.addWidget(Lb_Total, 4, 0)

        Grid.addWidget(LEd_Cliente, 0, 1, 1, 2)
        Grid.addWidget(LEd_Niver, 1, 1, 1, 2)
        Grid.addWidget(self.LEd_NumPrest, 2, 1, 1, 2)
        Grid.addWidget(self.LEd_ValPrest, 3, 1, 1, 2)
        Grid.addWidget(self.LEd_Total, 4, 1, 1, 2)

        Grid.addWidget(Bt_Calc, 5, 1)

        self.setLayout(Grid)
        self.show()

########################################################################################################################

App=QApplication(sys.argv)

Jan1=Janela("Minha janela", 400, 200, 480, 200, "orange")

App.exec_()
