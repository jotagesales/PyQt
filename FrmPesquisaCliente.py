# -*- coding: UTF-8 -*-

'''
Created on 03/05/2014

@author: jotage
'''
from Base import *

class FrmPesquisaCliente(Diaglog):
    
    def __init__(self, parent = None):
        super(FrmPesquisaCliente, self).__init__(parent)
        
        self.FrmPesquisaClienteCreate()
        
        self.CenterOnScreen()
        
    def FrmPesquisaClienteCreate(self):
        #=======================================================================
        # customizando a tela de pesquisa
        #=======================================================================
        self.setWindowTitle('Pesquisa de cliente')
        self.resize(500, 300)
        
        self.layoutPrincipal = LayoutVertical()
        
        # criando o campo de busca
        self.lblBusca = Label('Digite a busca', self)
        self.txtBusca = TextBox(self)
        
        hboxBusca = LayoutHorizontal()
        hboxBusca.addWidget(self.lblBusca)
        hboxBusca.addWidget(self.txtBusca)
        
        self.layoutPrincipal.addLayout(hboxBusca)
        
        # criando o grid da pesquisa
        cabecalh_grid = [u'Código', 'Nome', 'Cidade', 'UF']
        self.grdPesquisaCliente = Grid(self, 1, len(cabecalh_grid))        
        self.grdPesquisaCliente.setHorizontalHeaderLabels(cabecalh_grid)
        
        self.layoutPrincipal.addWidget(self.grdPesquisaCliente)
        
        self.setLayout(self.layoutPrincipal)
    
    def CenterOnScreen(self):
        '''alinhando a o formulario no centro da tela'''
        resolucao = QDesktopWidget().screenGeometry()
        self.move((resolucao.width() / 2) - (self.frameSize().width() / 2),
                  (resolucao.height() / 2) - (self.frameSize().height() / 2))
if __name__ == '__main__':
    import sys
    root = QApplication(sys.argv)
    app = FrmPesquisaCliente(None)
    app.show()
    root.exec_()