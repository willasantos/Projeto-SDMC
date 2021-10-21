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
        self.horizontalLayout.addWidget(self.table)
        self.cadastroAtual = None
        self.setEventos()
        self.carregaCadastro()
        self.data_nascimento.setDate(QDate.currentDate())
        self.data_consulta.setDate(QDate.currentDate())

    def setEventos(self):
        self.bt_salvar.clicked.connect(self.salveCadastro)
        self.bt_limpar.clicked.connect(self.limparCampos)
        self.bt_excluir.clicked.connect(self.excluirCadastro)  

    def carregaCadastro(self):
        self.lista_cadastro = CadModel.gettCadastro()
        lista_combo = []
        for cadastro in self.lista_cadastro:
            lista_combo.append(cadastro.especialidade)   
        self.combo_medico.addItems(lista_combo)

    def salveCadastro(self):
        novo = self.getCad()  
        if novo != None:
            if self.cadastroAtual == None:
                self.table.adicionar(novo)
            else:
                novo.id = self.cadastroAtual.id
                self.table.atualizar(novo)
            self.limparCampos()

    def getCad(self):
        nome = self.nome_com.text()
        cpf = self.cpf.text()
        cartao_sus = self.cartao_sus.text()
        telefone = self.telefone.text()
        endereco = self.endereco.text()     
        data = self.data_consulta.dateTime().toString('dd/MM/yyyy hh:mm')
        data_nascimento = self.data_nascimento.dateTime().toString('dd/MM/yyyy')
        especialidade = self.combo_medico.currentText()           

        if((nome != "")and (cpf != "") and (cartao_sus != "")and (telefone != "") and  (endereco != "") and (data != "") and (data_nascimento != "") and (especialidade != "")):
            return Cadastro(-1, nome, cpf, cartao_sus, telefone, endereco,data, data_nascimento, especialidade)
        return None

    def limparCampos(self):
        self.cadastroAtual = None
        self.nome_com.setText("")
        self.cpf.setText("")
        self.cartao_sus.setText("")
        self.telefone.setText("")
        self.endereco.setText("")
        self.data_nascimento.setDate(QDate.currentDate())
        self.data_consulta.setDate(QDate.currentDate())

        self.bt_salvar.setText("Salvar")
        self.bt_excluir.setEnabled(False)
        self.table.carregaDados()

    def inserirCampos(self, cadastro):
        self.cadastroAtual = cadastro
        self.nome_com.setText(cadastro.nome)
        self.cpf.setText(str(cadastro.cpf))
        self.cartao_sus.setText(str(cadastro.cartao_sus))
        self.telefone.setText(str(cadastro.telefone))
        self.endereco.setText(cadastro.endereco)
        self.data_nascimento.setDate(QDate.currentDate())
        self.data_consulta.setDate(QDate.currentDate())

        self.bt_salvar.setText("Atualizar")
        self.bt_excluir.setEnabled(True)

    def excluirCadastro(self):
        self.table.deletar(self.cadastroAtual)
        self.limparCampos()               

    def finalizaCadastro(self):
        data = self.data_consulta.dateTime().toString('dd/MM/yyyy hh:mm')
        data_nascimento = self.data_nascimento.dateTime().toString('dd/MM/yyyy')
        novoCadastro = (-1, data, data_nascimento)
        CadModel.addCadastro(novoCadastro)   

        self.limparCampos()            
 