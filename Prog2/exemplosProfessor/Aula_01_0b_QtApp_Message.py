from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

app = QApplication([])

QMessageBox.about(None, "Titulo da Janela", "Vou iniciar o programa!")

msg=QMessageBox()
msg.setIcon(QMessageBox.Information)
msg.setText("Isso é uma mensagem")
msg.setInformativeText("Informação adicional")
msg.setWindowTitle("Janela de Informação")
msg.setDetailedText("Informação detalhada")
msg.exec_()

QMessageBox.about(msg, "Titulo da Janela", "Vou encerrar o programa!")

app.exec_()