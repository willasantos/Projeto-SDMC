from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

import models.exame_model as ExModel

class QuadroExame(QTableWidget):
    def __init__(self, janela_prince):
        super().__init__(0, 6)
        self.janela_prince = janela_prince

        headers = ["ID", "NOME", "CPF", "TELEFONE", "DATA E HORA",  "EXAME"]
        self.setHorizontalHeaderLabels(headers)

        self.configuracao()
        self.carregaDados()

    def configuracao(self):
        self.verticalHeader().setVisible(False)

        self.horizontalHeader().setStretchLastSection(False) 
        self.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(3,QHeaderView.ResizeToContents)
        self.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.clicked.connect(self.on_click)     

    def carregaDados(self):
        self.lista_exame = ExModel.gettExame()
        self.setRowCount(0)
        for exame in self.lista_exame:
            self.addRow(exame) 

    def addRow(self, exame):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        id_paciente = QTableWidgetItem(str(exame.id_paciente))
        nome_paciente = QTableWidgetItem(exame.nome_paciente)
        data_hora = QTableWidgetItem(str(exame.data_hora))
        exame = QTableWidgetItem(exame.exame)
        cpf_paciente = QTableWidgetItem(str(exame.cpf_paciente))
        telefone_paciente = QTableWidgetItem(str(exame.telefone_paciente))
        
        self.setItem(rowCount, 0, id_paciente)
        self.setItem(rowCount, 1, nome_paciente)
        self.setItem(rowCount, 2, data_hora)
        self.setItem(rowCount, 3, exame)
        self.setItem(rowCount, 4, cpf_paciente)  
        self.setItem(rowCount, 5, telefone_paciente)

    def on_click(self):
        selected_row = self.currentRow()
        id_paciente = self.item(selected_row, 0).text()
        Exame = ExModel.getExame(id_paciente)
        self.janela_prince.inserirCampos(Exame)

    def adicionar(self, exame):
        ExModel.addExame(exame)
        self.carregaDados()  

    def atualizar(self, exame):
        ExModel.editExame(exame)
        self.carregaDados 

    def deletar(self, exame):
        ExModel.delExame(exame.id_paciente)
        self.carregaDados()                     
               