from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from classes.Cadastro import Cadastro
from componentes.table_cadastros import QuadroCadastro

class CadCadastro(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/cadastro.ui", self)
        self.table = QuadroCadastro(self)

        self.verticalLayout.addWidget(self.table)
        self.cadastroAtual = None
        self.setEventos()

    def setEventos(self):
        self.salvar.clicked.connect(self.salveCadastro)
        self.limpar.clicked.connect(self.limparCampos)
        self.excluir.clicked.connect(self.excluirCadastro)

    def salveCadastro(self):
        novo = self.gettCadastro()  
        if novo != None:
            if self.cadastroAtual == None:
                self.table.adicionar(novo)
            else:
                novo.id = self.cadastroAtual.id
                self.table.atualizar(novo)

            self.limparCampos()

    def getCad(self):
        nome = self.nome.text()
        cpf = self.cpf.text()
        cartao_sus = self.cartao_sus.text()
        telefone = self.telefone.text()
        endereco = self.endereco.text()                

        if((nome != "")and (cpf != "") and (cartao_sus != "")and (telefone != "") and (endereco != "")):
            return Cadastro(-1, nome, cpf, cartao_sus, telefone, endereco)
        return None

    def limparCampos(self):
        self.cadastroAtual = None
        self.nome.setText("")
        self.cpf.setText("")
        self.cartao_sus.setText("")
        self.telefone.setText("")
        self.endereco.setText("")

        self.salvar.setText("Salvar")
        self.excluir.setEnabled(False)
        self.table.carregaDados()

    def inserirCadastro(self, cadastro):
        self.cadastroAtual = cadastro
        self.nome.setText(cadastro.nome)
        self.cpf.setText(cadastro.cpf)
        self.cartao_sus.setText(cadastro.cartao_sus)
        self.telefone.setText(cadastro.telefone)
        self.endereco.setText(cadastro.endereco)

        self.salavar.setText("Atualizar")
        self.excluir.setenabled(True)

    def excluirCadastro(self):
        self.table.deletar(self.cadastroAtual)
        self.limparCampos()               