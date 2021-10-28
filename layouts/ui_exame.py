from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import  QDate
from PyQt5 import uic

from classes.exame import Exame
from componentes.table_exames import QuadroExame
import models.exame_model as ExModel

class NovoExame(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/exame.ui", self)
        self.table = QuadroExame(self)
        self.horizontalLayout.addWidget(self.table)
        self.exameAtual = None
        self.setEventos()
        self.carregaExame()
        self.data_hora.setDate(QDate.currentDate())

    def setEventos(self):
        self.adicionar.clicked.connect(self.salveExame)
        self.limpar.clicked.connect(self.limparCampos)
        self.remover.clicked.connect(self.excluirExame)  

    def carregaExame(self):
        self.lista_exame = ExModel.gettExame()
        lista_combo = []
        for exame in self.lista_exame:
            lista_combo.append(exame.exame)   
        self.combo_exame.addItems(lista_combo)    

    def salveExame(self):
        novo = self.getExa()  
        if novo != None:
            if self.exameAtual == None:
                self.table.adicionar(novo)
            else:
                novo.id = self.exameAtual.id_paciente
                self.table.atualizar(novo)
            self.limparCampos()       

    def getExa(self):
        nome_paciente = self.nome_paciente.text()
        data_hora = self.data_hora.dateTime().toString('dd/MM/yyyy hh:mm')
        exame = self.combo_exame.currentText()
        cpf_paciente = self.cpf_paciente.text()
        telefone_paciente = self.telefone_paciente.text()              

        if((nome_paciente != "")and (data_hora != "") and (exame != "")and (cpf_paciente != "") and  (telefone_paciente != "")):
            return Exame(-1, nome_paciente, data_hora, exame, cpf_paciente, telefone_paciente)
        return None
    
    def limparCampos(self):
        self.exameAtual = None
        self.nome_paciente.setText("")
        self.data_hora.setDate(QDate.currentDate())
        self.cpf_paciente.setText("")
        self.telefone_paciente.setText("")
    
        self.adicionar.setText("Adicionar")
        self.remover.setEnabled(False)
        self.table.carregaDados()

    def inserirCampos(self, exame):
        self.exameAtual = exame
        self.nome_paciente.setText(exame.nome_paciente)
        self.data_hora.setDate(QDate.currentDate())
        self.cpf_paciente.setText(str(exame.cpf_paciente))
        self.telefone_paciente.setText(str(exame.telefone_paciente))

        self.adicionar.setText("Atualizar")
        self.remover.setEnabled(True)   

    def excluirExame(self):
        self.table.deletar(self.exameAtual)
        self.limparCampos()    

    def finalizarExame(self):
        data_hora = self.data_hora.dateTime().toString('dd/MM/yyyy hh:mm')
        novoExame = (-1, data_hora)
        ExModel.addExame(novoExame)   

        self.limparCampos()            