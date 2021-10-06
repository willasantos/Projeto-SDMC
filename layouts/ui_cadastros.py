from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from classes.Cadastro import Cadastro
from componentes.table_cadastros import QuadroCadastro

class CadCadastro(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/cadastro.ui", self)
        self.table = QuadroCadastro(self)

        self.horizontalLayout.addWidget(self.table)
        self.cadAtual = None
        self.setEventos()

    def setEventos(self):
        self.salvar.clicked.connect(self.salveCadastro)
        self.atualizar.clicked.connect(self.atualizeCadastro)
        self.excluir.clicked.connect(self.excluirCadastro)

