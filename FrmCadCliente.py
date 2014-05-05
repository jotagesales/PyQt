# -*- coding: UTF-8 -*-
'''
Created on 03/05/2014

@author: jotage
'''
from FrmcadDefault import FrmCadDefault
from PyQt4.QtGui import QApplication
from Base import *
from FrmPesquisaCliente import FrmPesquisaCliente

class FrmCadCliente(FrmCadDefault):
    
    def __init__(self, parent = None):
        super(FrmCadCliente, self).__init__(parent)
        
        self.FrmCadClienteCreate()
        
        self.btnPesquisar.clicked.connect(self.AbrePesquisa)
        self.btnSalvar.clicked.connect(self.Imprime)
        
        
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
        
    def Imprime(self):
        print self.txtCPF.text()
        print self.txtNome.text()
        print self.txtLogradouro.text()
        
        print self.txtNumero.text()
        print self.txtCodigo.text()
        
    


if __name__ == '__main__':
    import sys
    root = QApplication(sys.argv)
    app = FrmCadCliente(None)
    app.show()
    root.exec_()