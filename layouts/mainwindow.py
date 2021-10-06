from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from layouts.ui_cadastros import CadCadastro

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/mainwindow.ui", self)

        self.listWidget.setCurrentRow(0)
        self.mostrarJanelas()
        self.listWidget.currentRowChanged.connect(self.display)
        self.setEventos()
       

    def setEventos(self):
        self.btn_entrar.clicked.connect(self.Iniciar)

    def Iniciar(self):
        self.stackedWidget.setCurrentIndex(1)
        self.statusbar.showMessage("Usuário: recepcionista")

    def mostrarJanelas(self):
        self.stackedWidget.insertWidget(0, CadCadastro())

    def display(self, index):
        self.mostrarJanelas()
        self.stackedWidget.setCurrentIndex(index) 
        self.listWidget.setCurrentRow(index)   
