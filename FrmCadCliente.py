# -*- coding: UTF-8 -*-
'''
Created on 03/05/2014

@author: jotage
'''
from FrmcadDefault import FrmCadDefault
from PyQt4.QtGui import QApplication
from Base import *
from FrmPesquisaCliente import FrmPesquisaCliente
from Db import Db, ClientesDb

class FrmCadCliente(FrmCadDefault):
    
    def __init__(self, parent = None):
        super(FrmCadCliente, self).__init__(parent)
        
        self.FrmCadClienteCreate()

        #criando um objeto cliente DB ara que fique a disposição para interagir com o módulo de acesso a dados
        self.clientedb = ClientesDb()
        
        # conectando os clicks dos botoes as devidas funçoes
        self.btnPesquisar.clicked.connect(self.AbrePesquisa)
        self.btnSalvar.clicked.connect(self.Salvar)
        self.btnExcluir.clicked.connect(self.__Excluir)

        
        
    def FrmCadClienteCreate(self):
        self.setWindowTitle('Cadastro de clientes')
        self.setWindowState(Qt.WindowMaximized)
        
        # criando os campos de cadastro
        self.txtCPF = TextBox(self)
        self.txtCPF.setFixedWidth(170)        
        
        self.txtNome = TextBox(self)
        
        self.txtLogradouro = TextBox(self)
        self.txtNumero = TextBox(self)
        self.txtBairro = TextBox(self)
        self.txtCidade = TextBox(self)
        
        self.txtUF = TextBox(self)
        self.txtUF.setFixedWidth(170)
        self.txtUF.setMaxLength(2)
        
        # adicionando os campos no form layout da base de cadastro
        self.fLayout.addRow('CPF', self.txtCPF)
        self.fLayout.addRow('Nome', self.txtNome)
        self.fLayout.addRow('Logradouro', self.txtLogradouro)
        self.fLayout.addRow(u'Número', self.txtNumero)
        self.fLayout.addRow('Bairro', self.txtBairro)
        self.fLayout.addRow('Cidade', self.txtCidade)
        self.fLayout.addRow('UF', self.txtUF)
        
    def AbrePesquisa(self):
        frmPesquisa = FrmPesquisaCliente(self)
        frmPesquisa.setModal(True)
        frmPesquisa.show()
        frmPesquisa.exec_()
        
    def Salvar(self):
        try:
            #capturando os dados da tela
            Codigo = self.txtCodigo.text()
            CPF = self.txtCPF.text()
            Nome = self.txtNome.text()
            Logradouro = self.txtLogradouro.text()
            Numero = int(self.txtNumero.text())
            Bairro =self.txtBairro.text()
            Cidade = self.txtBairro.text()
            UF = str(self.txtUF.text()).upper()

            if Codigo == '':
                self.__inserir(Codigo, CPF, Nome, Logradouro, Numero, Bairro, Cidade, UF)
                msg = MessageBox()
                msg.information(self, 'Cadastro de clientes', 'CListe salvo com sucesso !!!', MessageBox.Ok)
            else:
                pass
        except Exception, e:
            msg = MessageBox()
            msg.critical(self, 'Cadastro de clientes', 'Ocorreu o seguinte erro ao tentar inserir o cliente: \n ' + str(e), MessageBox.Ok)
    
    def __inserir(self, id, cpf, nome, logradouro, numero, bairro, cidade, uf):
        '''Método cria um objeto cliente do modulo de acesso a dados, e inclui um novo cliente no banco'''
        
        self.clientedb.Salvar(id, cpf, nome, logradouro, numero, bairro, cidade, uf)

    def __Excluir(self, pId):
        try:
            codigo = int(self.txtCodigo.text())
            self.clientedb.Excluir(codigo)
            
        except Exception, e:
            msg = MessageBox()
            msg.critical(self, 'Cadastro de clientes', 'Ocorreu o seguinte erro ao tentar excluir: \n ' + str(e).decode('utf8'), MessageBox.Ok)


if __name__ == '__main__':
    import sys
    root = QApplication(sys.argv)
    app = FrmCadCliente(None)
    app.show()
    root.exec_()