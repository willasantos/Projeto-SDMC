from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QRegExp, QDate
from PyQt5 import uic

import models.cadastros_model as CadModel

class NovoExame(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/exame.ui", self)

        self.cadastroAtual = None
        self.lista_cadastro = []
        self.lista_exames = []

        self.setEventos()
        self.carregaConsulta()
        self.carregaExames()

    def carregaConsulta(self):
        self.lista_cadastro = CadModel.gettCadastro()
        lista_combo = []
        for cadastro in self.lista_cadastro:
            lista_combo.append(cadastro.nome)    
        self.combo_paciente.addItems(lista_combo)

    def carregaExames(self):
        self.lista_exames = CadModel.gettCadastro()
        lista_combo = []
        for e in self.lista_exames:
            lista_combo.append(e.nome)
        self.combo_exame.addItems(lista_combo)              

    def setEventos(self):
        self.adicionar.clicked.connect(self.Adicionar)
        self.limpar.clicked.connect(self.Limpar)
        self.remover.clicked.connect(self.RemoverExame)

    def Adicionar(self):
        self.adicionar.setEnabled(True)
        self.remover.setEnabled(False)

    def Limpar(self):
        self.limpar.setEnabled(True)

    def RemoverExame(self):
        self.adicionar.setEnabled(False)
        self.remover.setEnabled(True)        