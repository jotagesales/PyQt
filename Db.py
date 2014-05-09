# -*- coding: UTF-8 -*-

import sqlite3

class Db(object):
	'''A classe Db representa o banco de dados, ela fornece os seguintes objetos
	conn = connection
	cursor = cursor para execução de instruções sql
	'''
	def __init__(self):
		self.conn = sqlite3.connect('video_aula.db')
		self.cursor = self.conn.cursor()


class ClientesDb(object):
	'''A classe ClientesDb representa um cliente no banco de dados, tendo os seguintes métodos:

	PUBLICOS:
	- Salvar()
	- Excluir()
	- ConsultaTodosClientes()

	PRIVADOS:
	- __IncluirNovo()
	- __Alterar()

	'''
	def __init__(self):
		#instanciando um objeto que representa o banco, este objeto tem uma connection e um cursor
		self.banco = Db()

	def Salvar(self, pId, pCPF, pNome, pLogradouro, pNumero, pBairro, pCidade, pUF):
		'''método recebe os parametros de cliente e toma decisão se vai criar um novo ou alterar um existente'''
		
		# recebendo os parametros
		self.Id = pId
		self.Nome = pNome
		self.Logradouro = pLogradouro
		self.Numero = pNumero
		self.Bairro = pBairro
		self.Cidade = pCidade
		self.UF = pUF
		
		# verificando se vai incluir um novo ou alterar um existente
		if self.Id == '':
			self.__IncluirNovo()
		else:
			self.__Alterar()

	def __IncluirNovo(self):
		'''Inclui novo cliente no banco'''

		#montando o sql de insert na tabela de clientes
		sql = 'INSERT INTO CLIENTES(Nome, Logradouro, Numero, Bairro, Cidade, UF)\
									values("%s", "%s", "%i","%s","%s","%s")' %(self.Nome,
																			   self.Logradouro,
																			   self.Numero,
																			   self.Bairro,
																			   self.Cidade,
																			   self.UF
																			)
		self.banco.cursor.execute(sql)
		self.banco.conn.commit()

	def __Alterar(self, pId):
		'''Alterar um cliente existente no banco'''
		pass

	def Excluir(self, pId):
		'''Recebe um id e exclui o registro do banco caso ele exista'''

		try:
			cliente = self.ConsultaCliente(pId)

			# verificando se existe cliente com o ID passado, caso nao exista gera exceção
			if cliente:
				sql = 'DELETE FROM CLIENTES WHERE id = "%i"' %(pId)
				self.banco.cursor.execute(sql)
				self.banco.conn.commit()
			else:
				raise Exception('Não exite cliente com o código informado')

		except Exception, e:
			raise Exception('Não foi possíel excluir o registro: \n Messagem original: ' + str(e))



	def ConsultaCliente(self, pId):
		'''Método consulta os dados do cliente passado o id como parâmetro'''
		sql = 'SELECT * FROM CLIENTES WHERE id = "%i"' %(pId)
		resultado = self.banco.cursor.execute(sql)
		return resultado.fetchone()
		
	def ConsultaTodosClientes(self):
		sql = 'SELECT * FROM CLIENTES'
		resultado = self.banco.cursor.execute(sql)
		return resultado.fetchall()

	def ConsultaClientesPorNome(self, pNome = ''):
		print 'parametro:' + pNome
		sql = 'SELECT id, Nome, Cidade, UF FROM CLIENTES WHERE Nome like("%' + pNome + '%")'
		resultado = self.banco.cursor.execute(sql)
		return resultado.fetchall()


if __name__ == '__main__':
	cliente = ClientesDb()

	# tbl_clientes = 'CREATE TABLE CLIENTES(id integer not null primary key,\
	# 							Nome Varchar(100) not null,\
	# 							Logradouro Varchar(100) not null,\
	# 							Numero integer not null,\
	# 							Bairro Varchar(50) not null,\
	# 							Cidade Varchar(80) not null,\
	# 							UF Varchar(2) not null )'