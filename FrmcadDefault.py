# -*- coding: UTF-8 -*-


'''
Created on 03/05/2014

@author: jotage
'''
from Base import *

class FrmCadDefault(Widget):
    
    def __init__(self, parent= None):
        super(FrmCadDefault, self).__init__(parent)
        
        self.FrmCadDefaultCreate()
        
    def FrmCadDefaultCreate(self):
        #=======================================================================
        # CUSTOMIZANDO A JANETA
        #=======================================================================
        self.setWindowTitle(u'Cadastro padrão')
        
        self.layoutPrincipal = LayoutVertical()
        
        self.txtCodigo = TextBox(self)
        self.txtCodigo.setFixedWidth(170)
        
        self.ckAtivo = CheckBox('Ativo', self)
        self.ckAtivo.setChecked(True)
        
        hboxcodigo = LayoutHorizontal()
        hboxcodigo.addWidget(self.txtCodigo)
        hboxcodigo.addWidget(self.ckAtivo)
        hboxcodigo.addStretch(2)
        
        self.fLayout = FormLayout()
        self.fLayout.addRow(u'Código', hboxcodigo)
        
        #adicionando o form layout ao layout rincipal
        self.layoutPrincipal.addLayout(self.fLayout)
        
        #=======================================================================
        # CRIANDO OS BOTOES
        #=======================================================================
        self.btnNovo = Botao('&Novo', self)
        self.btnSalvar = Botao('&Salvar', self)
        self.btnPesquisar = Botao('&Pesquisar', self)
        
        hboxBotoes = LayoutHorizontal()
        hboxBotoes.addStretch(2)
        hboxBotoes.addWidget(self.btnNovo)
        hboxBotoes.addWidget(self.btnSalvar)
        hboxBotoes.addWidget(self.btnPesquisar)
        hboxBotoes.setSpacing(1)
        
        
        #adicionando os botoes ao layout principal
        self.layoutPrincipal.addLayout(hboxBotoes)
        
        self.setLayout(self.layoutPrincipal)


if __name__ == '__main__':
    import sys
    root = QApplication(sys.argv)
    app = FrmCadDefault(None)
    app.show()
    root.exec_()