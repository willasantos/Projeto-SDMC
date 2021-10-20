from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidget, QTableWidgetItem, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5 import uic

class InformacaoConsulta(QWidget):
    def __init__(self):
         super().__init__()
         uic.loadUi("ui/info.ui", self)
         

   