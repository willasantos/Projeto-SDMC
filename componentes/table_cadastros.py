from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

import models.cadastros_model as CadModel

class QuadroCadastro(QTableWidget):
    def __init__(self, janela_prince):
        super().__init__(0, 6)
        self.janela_prince = janela_prince

        headers = ["ID", "NOME", "CPF", "CARTAO_SUS", "TELEFONE", "ENDERECO", "DATA", "DATA_NASCIMENTO"]
        self.setHorizontalHeaderLabels(headers)   

        self.configuracao()
        self.carregaDados()

    def configuracao(self):
        self.verticalHeader().setVisible(False)

        self.horizontalHeader().setStretchLastSection(False) 
        self.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(3,QHeaderView.ResizeToContents)

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
        cpf = QTableWidgetItem(cadastro.cpf)
        cartao_sus = QTableWidgetItem(cadastro.cartao_sus)
        telefone = QTableWidgetItem(cadastro.telefone)
        endereco = QTableWidgetItem(cadastro.endereco)
        
    
        self.setItem(rowCount, 0, id)
        self.setItem(rowCount, 1, nome)
        self.setItem(rowCount, 2, cpf)
        self.setItem(rowCount, 3, cartao_sus)
        self.setItem(rowCount, 4, telefone)  
        self.setItem(rowCount, 5, endereco)      

    def on_click(self):
        selected_row = self.current_Row()
        id = self.item(selected_row, 0).text()
        cadastro = CadModel.getCadastro(id)
        self.janela_prince.insereInfo(cadastro)

    def adicionar(self, cadastro):
        CadModel.addCadastro(cadastro)
        self.carregaDados()

    def atualizar(self, cadastro):
        CadModel.editCadastro(cadastro)
        self.carregaDados

    def deletar(self, cadastro):
        CadModel.delCadastro(cadastro.id)
        self.carregaDados()                           