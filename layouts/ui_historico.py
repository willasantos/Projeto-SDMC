from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidget, QTableWidgetItem, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5 import uic

import models.cadastros_model as CadModel
import layouts.ui_info as Info

TYPE = {'remove': 0, 'info': 1}

class HistoricoConsulta(QWidget):
    def __init__(self, cadastro ):
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
            
            self.tableWidget.setCellWidget(
            rowCount, 0, MeuBotao(item, self, TYPE['info']))
            self.tableWidget.setItem(rowCount, 1, id)
            self.tableWidget.setItem(rowCount, 2, nome)
            self.tableWidget.setItem(rowCount, 3, cpf)
            self.tableWidget.setItem(rowCount, 4, data)
            self.tableWidget.setItem(rowCount, 5, especialidade)
            self.tableWidget.setCellWidget(
            rowCount, 6, MeuBotao(item, self, TYPE['remove']))

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
        else:
            self.typeInfo()    
    
        self.btn.setStyleSheet(
            'QPushButton {background-color: #00FFFFFF; border:  none}')

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def typeInfo(self):
        self.btn.setIcon(QIcon("icons/informações.png.png"))  
        #self.btn.clicked.connect(self.maisInfo)
        self.btn.setToolTip(
            "Mais informações ") 
        self.btn.setIconSize(QSize(25, 25))    

    def typeDelete(self):
        self.btn.setIcon(QIcon("icons/Button delete.png"))  
        self.btn.clicked.connect(self.remover)
        self.btn.setToolTip(
            "Remover cadastro ?") 

        self.btn.setIconSize(QSize(20, 20))

    def remover(self):
        pass
"""
    def maisInfo(self):
        self.w = Info(self.info)
        self.w.show()"""