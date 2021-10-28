from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidget, QTableWidgetItem, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5 import uic

import models.exame_model as ExModel

class HistoricoExame(QWidget):
    def __init__(self):
         super().__init__()
         uic.loadUi("ui/hist_exame.ui", self)

         self.exameAtual = None
         self.configTable()
         self.inserirDados(self)    

    def inserirDados(self, item):
        lista_exame = ExModel.gettExame()

        for e in lista_exame:
            rowCount = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowCount)

            id = QTableWidgetItem(str(e.id_paciente))
            id.setTextAlignment(Qt.AlignCenter)    
            nome = QTableWidgetItem(e.nome_paciente)
            nome.setTextAlignment(Qt.AlignCenter) 
            data = QTableWidgetItem(str(e.data_hora))
            data.setTextAlignment(Qt.AlignCenter)
            exames = QTableWidgetItem(e.exame)
            exames.setTextAlignment(Qt.AlignCenter)
    
            self.tableWidget.setItem(rowCount, 0, id)
            self.tableWidget.setItem(rowCount, 1, nome)
            self.tableWidget.setItem(rowCount, 2, data)
            self.tableWidget.setItem(rowCount, 3, exames)  

    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                 QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  
           