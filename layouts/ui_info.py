from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidget, QTableWidgetItem, QHBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5 import uic

class InformacaoConsulta(QWidget):
    def __init__(self, cadastro):
         super().__init__()
         uic.loadUi("ui/info.ui", self)

         self.venda = cadastro