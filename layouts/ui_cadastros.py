from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from PyQt5.QtCore import  QDate

from classes.Cadastro import Cadastro
from componentes.table_cadastros import QuadroCadastro
import models.cadastros_model as CadModel

class CadCadastro(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/cadastro.ui", self)
        self.table = QuadroCadastro(self)

        self.verticalLayout.addWidget(self.table)
        self.cadastroAtual = None
        self.setEventos()
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit_2.setDate(QDate.currentDate())

    def setEventos(self):
        self.bt_salvar.clicked.connect(self.salveCadastro)
        self.bt_limpar.clicked.connect(self.limparCampos)
        self.bt_excluir.clicked.connect(self.excluirCadastro)  
        self.combo_medico.currentIndexChanged(self.text_edited)

    def text_edited(self, c):
        self.table.carregaDados(c)        

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
        data = self.data.text()
        data_nascimento = self.data_nascimento.text()
        especialidade = self.especialidade.text()           

        if((nome != "")and (cpf != "") and (cartao_sus != "")and (telefone != "") and (endereco != "") and (data != "") and (data_nascimento != "") and (especialidade != "")):
            return Cadastro(-1, nome, cpf, cartao_sus, telefone, endereco, data, data_nascimento, especialidade)
        return None

    def limparCampos(self):
        self.cadastroAtual = None
        self.nome.setText("")
        self.cpf.setText("")
        self.cartao_sus.setText("")
        self.telefone.setText("")
        self.endereco.setText("")
        self.especialidade.setText("")

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
        self.data.setText(cadastro.data)
        self.data_nascimento.setText(cadastro.data_nascimento)
        self.especialidade.setText(cadastro.especialidade)

        self.salvar.setText("Atualizar")
        self.excluir.setenabled(True)

    def excluirCadastro(self):
        self.table.deletar(self.cadastroAtual)
        self.limparCampos()               

    def finalizaCadastro(self):
        data = self.dateEdit.dateTime().toString('dd/MM/yyyy')
        data_nascimento = self.dateEdit_2.dateTime().toString('dd/MM/yyyy')
        novoCadastro = (-1, data_nascimento, data)
        CadModel.addCadastro(novoCadastro)   

        self.limparCampos()            