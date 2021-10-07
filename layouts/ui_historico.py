from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QIcon
from PyQt5 import uic

import models.cadastros_model as CadModel

TYPE = {'remove': 0}

class HistoricoConsulta(QWidget):
    def __init__(self, cadastro):
         super().__init__()
         uic.loadUi("ui/historico.ui", self)

         self.cadastro = cadastro
         self.configTable()
         self.inserirDados()
         
    def inserirDados(self):
        lista_consultas = CadModel.getCadastro(self.cadastro.id)

        for c in lista_consultas:
            rowCount = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowCount)

            id = QTableWidgetItem(str(c.id))
            id.setTextAlignment(Qt.AlignCenter)    
            nome = QTableWidgetItem(c.nome)
            nome.setTextAlignment(Qt.AlignCenter) 
            cpf = QTableWidgetItem(str(c.cpf))
            cpf.setTextAlignment(Qt.AlignCenter)

            self.tableWidget.setItem(rowCount, 0, id)
            self.tableWidget.setItem(rowCount, 1, nome)
            self.tableWidget.setItem(rowCount, 2, cpf)

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

class MeuBotao(QWidget):
    def __init__(self, historico, pai, type):
        super(MeuBotao, self).__init__()
        self.historico = historico
        self.pai = pai

        self.w = None

        self.btn = QPushButton(self)
        self.btn.setText("") 

        if type == TYPE['remove']:
            self.typeDelete()
    
        self.btn.setStyleSheet(
            'QPushButton {background-color: #00FFFFFF; border:  none}')

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def typeDelete(self):
        self.btn.setIcon(QIcon("icons/Button delete"))  
        self.btn.clicked.connect(self.remover)
        self.btn.setToolTip(
            "Remover venda?") 

        self.btn.setIconSize(QSize(20, 20))

    def remover(self):
        pass
