from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

import models.cadastros_model as CadModel

class QuadroCadastro(QTableWidget):
    def __init__(self, janela_prince):
        super().__init__(0, 9)
        self.janela_prince = janela_prince

        headers = ["ID", "NOME", "CPF", "CARTAO_SUS", "FONE", "ENDERECO", "DATA", "NASCIMENTO", "MEDICO"]
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
        self.lista_cadastro = CadModel.gettCadastro()
        self.setRowCount(0)
        for cadastro in self.lista_cadastro:
            self.addRow(cadastro)

    def addRow(self, cadastro):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        id = QTableWidgetItem(str(cadastro.id))
        nome = QTableWidgetItem(cadastro.nome)
        cpf = QTableWidgetItem(str(cadastro.cpf))
        cartao_sus = QTableWidgetItem(str(cadastro.cartao_sus))
        telefone = QTableWidgetItem(str(cadastro.telefone))
        endereco = QTableWidgetItem(cadastro.endereco)
        data = QTableWidgetItem(cadastro.data)
        data_nascimento = QTableWidgetItem(cadastro.data_nascimento)
        especialidade = QTableWidgetItem(cadastro.especialidade)
        
        self.setItem(rowCount, 0, id)
        self.setItem(rowCount, 1, nome)
        self.setItem(rowCount, 2, cpf)
        self.setItem(rowCount, 3, cartao_sus)
        self.setItem(rowCount, 4, telefone)  
        self.setItem(rowCount, 5, endereco)  
        self.setItem(rowCount, 6, data)  
        self.setItem(rowCount, 7, data_nascimento) 
        self.setItem(rowCount, 8, especialidade)       

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        cadastro = CadModel.getCadastro(id)
        self.janela_prince.inserirCampos(cadastro)

    def adicionar(self, cadastro):
        CadModel.addCadastro(cadastro)
        self.carregaDados()

    def atualizar(self, cadastro):
        CadModel.editCadastro(cadastro)
        self.carregaDados

    def deletar(self, cadastro):
        CadModel.delCadastro(cadastro.id)
        self.carregaDados()                           