from PyQt5.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QWidget, QListWidgetItem
from PyQt5 import uic
from layouts.ui_cadastros import CadCadastro
from layouts.ui_historico import HistoricoConsulta

class CustomQWidget(QWidget):
    def __init__(self, icon, text, parent=None):
        super(CustomQWidget, self).__init__(parent)

        label_icon = QLabel(icon)
        label_text = QLabel(text)

        layout = QHBoxLayout()
        layout.addWidget(label_icon)
        layout.addWidget(label_text)
        layout.addWidget(label_icon)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/mainwindow.ui", self)

        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget("+", "MARCAR CONSULTA")
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.insertItem(0,item)
        self.listWidget.setItemWidget(item, item_widget)

        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget("+", "HISTORICO CONSULTA")
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.insertItem(1,item)
        self.listWidget.setItemWidget(item, item_widget) 

        self.listWidget.setCurrentRow(0)
        self.mostrarJanelas()
        self.listWidget.currentRowChanged.connect(self.display)
        self.btn_entrar.clicked.connect(self.Iniciar)

    def Iniciar(self):
        self.stackedWidget.setCurrentIndex(1)
        self.statusbar.showMessage("Usuário: recepcionista")

    def mostrarJanelas(self):
        self.stackedWidget.insertWidget(0, CadCadastro())
        self.stackedWidget.insertWidget(1, HistoricoConsulta(self))

    def display(self, index):
        self.mostrarJanelas()
        self.stackedWidget.setCurrentIndex(index) 
        self.listWidget.setCurrentRow(index)   
