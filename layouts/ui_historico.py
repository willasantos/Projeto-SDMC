from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidget, QTableWidgetItem, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5 import uic

import models.cadastros_model as CadModel

class HistoricoConsulta(QWidget):
    def __init__(self):
         super().__init__()
         uic.loadUi("ui/historico.ui", self)

         self.cadastroAtual = None
         self.configTable()
         self.inserirDados(self)
             
    def inserirDados(self, item):
        lista_cadastro = CadModel.gettCadastro()

        for c in lista_cadastro:
            rowCount = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowCount)

            id = QTableWidgetItem(str(c.id))
            id.setTextAlignment(Qt.AlignCenter)    
            nome = QTableWidgetItem(c.nome)
            nome.setTextAlignment(Qt.AlignCenter) 
            cpf = QTableWidgetItem(str(c.cpf))
            cpf.setTextAlignment(Qt.AlignCenter)
            data = QTableWidgetItem(str(c.data))
            data.setTextAlignment(Qt.AlignCenter)
            especialidade = QTableWidgetItem(str(c.especialidade))
            especialidade.setTextAlignment(Qt.AlignCenter)
    
            self.tableWidget.setItem(rowCount, 0, id)
            self.tableWidget.setItem(rowCount, 1, nome)
            self.tableWidget.setItem(rowCount, 2, cpf)
            self.tableWidget.setItem(rowCount, 3, data)
            self.tableWidget.setItem(rowCount, 4, especialidade)

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

