# -*- coding: UTF-8 -*-

'''
Created on 03/05/2014

@author: jotage
'''
from Base import *
from Db import ClientesDb

class FrmPesquisaCliente(Diaglog):
    
    def __init__(self, parent = None):
        super(FrmPesquisaCliente, self).__init__(parent)
        
        self.FrmPesquisaClienteCreate()

        #conectando o click dos botoes
        self.btnBuscar.clicked.connect(self.PesquisarCliente)


        #criando um objeto cliente DB ara que fique a disposição para interagir com o módulo de acesso a dados
        self.clientedb = ClientesDb()
        
        self.CenterOnScreen()
        
    def FrmPesquisaClienteCreate(self):
        #=======================================================================
        # customizando a tela de pesquisa
        #=======================================================================
        self.setWindowTitle('Pesquisa de cliente')
        self.resize(800, 300)
        
        self.layoutPrincipal = LayoutVertical()
        
        # criando o campo de busca
        self.lblBusca = Label('Digite a busca', self)
        self.txtBusca = TextBox(self)
        self.btnBuscar = Botao('&Buscar', self)
        
        hboxBusca = LayoutHorizontal()
        hboxBusca.addWidget(self.lblBusca)
        hboxBusca.addWidget(self.txtBusca)
        hboxBusca.addWidget(self.btnBuscar)

        
        self.layoutPrincipal.addLayout(hboxBusca)
        
        # criando o grid da pesquisa
        cabecalh_grid = [u'Código', 'Nome', 'Cidade', 'UF']
        self.grdPesquisaCliente = Grid(self, 0, len(cabecalh_grid))        
        self.grdPesquisaCliente.setHorizontalHeaderLabels(cabecalh_grid)

        #desativando edição do grid de pesquisa
        self.grdPesquisaCliente.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #recidimencionando as colunas do grid
        self.grdPesquisaCliente.setColumnWidth(1,300)
        self.grdPesquisaCliente.setColumnWidth(2, 200)

        self.layoutPrincipal.addWidget(self.grdPesquisaCliente)
        
        self.setLayout(self.layoutPrincipal)
    
    def PesquisarCliente(self, e):
        '''Método faz uma busca de clientes no banco de dados, e cria uma lista de tuplas'''
        # faz a consulta no banco e recebe uma lista de tuplas
        texto_busca = str(self.txtBusca.text())
        lista_dados_cliente = self.clientedb.ConsultaClientesPorNome(texto_busca)
        
        # setando no grid a qtde de linhas, com a mesma qtde de registros da lista
        qtde_registros = len(lista_dados_cliente)
        self.grdPesquisaCliente.setRowCount(qtde_registros)

        linha = 0
        for cliente in lista_dados_cliente:
            # capturando os dados da tupla
            id_cliente = cliente[0]
            Nome_cliente = cliente[1]
            cidade_cliente = cliente[2]
            UF_cliente = cliente[3]

            #preencendo o grid de pesquisa
            self.grdPesquisaCliente.setItem(linha, 0, QTableWidgetItem(id_cliente))
            self.grdPesquisaCliente.setItem(linha, 1, QTableWidgetItem(Nome_cliente))
            self.grdPesquisaCliente.setItem(linha, 2, QTableWidgetItem(cidade_cliente))
            self.grdPesquisaCliente.setItem(linha, 3, QTableWidgetItem(UF_cliente))

            linha += 1

    def CenterOnScreen(self):
        '''alinhando a o formulario no centro da tela'''
        resolucao = QDesktopWidget().screenGeometry()
        self.move((resolucao.width() / 2) - (self.frameSize().width() / 2),
                  (resolucao.height() / 2) - (self.frameSize().height() / 2))


if __name__ == '__main__':
    import sys
    root = QApplication(sys.argv)
    app = FrmPesquisaCliente()
    app.show()
    root.exec_()