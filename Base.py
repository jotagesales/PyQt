# -*- coding: UTF-8 -*-

'''
Created on 03/05/2014

@author: jotage
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *


class TextBox(QLineEdit):
    
    def __init__(self, parent = None):
        super(TextBox, self).__init__(parent)
        
class Label(QLabel):
    
    def __init__(self, pText= '', parent = None):
        super(Label, self).__init__(parent)
        
        self.setText(pText)
        
class CheckBox(QCheckBox):
    
    def __init__(self,pText= '', parent = None):
        super(CheckBox, self).__init__(parent)
        
        self.setText(pText)
        
class Botao(QPushButton):
    
    def __init__(self,pText= '', parent = None):
        super(Botao, self).__init__(parent)
        
        self.setText(pText)
        
        
class LayoutVertical(QVBoxLayout):
    
    def __init__(self):
        super(LayoutVertical, self).__init__()
        
class LayoutHorizontal(QHBoxLayout):
    
    def __init__(self):
        super(LayoutHorizontal, self).__init__()
        
class FormLayout(QFormLayout):
    
    def __init__(self):
        super(FormLayout, self).__init__()
        
class Widget(QWidget):
    
    def __init__(self, parent = None):
        super(Widget, self).__init__(parent)
        
class Diaglog(QDialog):
    
    def __init__(self, parent = None):
        super(Diaglog, self).__init__(parent)
        
class Grid(QTableWidget):
    
    def __init__(self, parent = None , qtde_linhas = 0, qtde_colunas = 0):
        super(Grid, self).__init__(parent)
        
        self.setRowCount(qtde_linhas)
        self.setColumnCount(qtde_colunas)
        
                
        #redimenciona a linha automaticamente
        self.resizeRowsToContents()
        
        #coloca as linhas em cores alternadas
        self.setAlternatingRowColors(True) 
        
        #habilita a ordenação ao clicar no titulo da coluna
        self.setSortingEnabled(True)
        
        #seleciona toda a linha quando clicado
        self.setSelectionBehavior(QAbstractItemView.SelectRows)

class MessageBox(QMessageBox):
    
    def __init__(self, parent = None):
        super(MessageBox, self).__init__(parent)


if __name__ == '__main__':
    import sys
    root = QApplication(sys.argv)
    m = MessageBox()
    help(m)