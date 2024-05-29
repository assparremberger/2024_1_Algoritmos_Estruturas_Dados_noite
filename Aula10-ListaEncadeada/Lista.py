from No import No

class Lista:
	def __init__(self):
		self.inicio = None
		self.tamanho = 0

	# def adicionarNoInicio(self, valor):
	# 	nodo = No(valor)
	# 	if self.inicio == None:
	# 		self.inicio = nodo
	# 	else: 
	# 		nodo.proximo = self.inicio
	# 		self.inicio = nodo
	# 	self.tamanho += 1
	# 	self.imprimir()

	def adicionarNoInicio(self, valor):
		nodo = No(valor)
		if self.inicio != None:
			nodo.proximo = self.inicio
		self.inicio = nodo
		self.tamanho += 1
		self.imprimir()

	def adicionarNoFim(self, valor):
		nodo = No(valor)
		if self.inicio == None:
			self.inicio = nodo
		else: 
			aux = self.inicio
			while aux.proximo:
				aux = aux.proximo
			aux.proximo = nodo
		self.tamanho += 1
		self.imprimir()
	
	def imprimir(self):
		print( "-----------------------------------" )
		if self.inicio == None:
			print( "Lista vazia" )
		else:
			print("Lista Encadeada com ", self.tamanho, " elementos")
			aux = self.inicio
			while aux:
				print( aux.dado )
				aux = aux.proximo

	# def removerDoInicio(self):
	# 	if self.inicio == None:
	# 		print( "Lista vazia" )
	# 	elif self.inicio.proximo == None:
	# 		self.inicio = None
	# 		self.tamanho = 0
	# 	else:
	# 		self.inicio = self.inicio.proximo
	# 		self.tamanho -= 1
	# 	self.imprimir()
	def removerDoInicio(self):
		if self.inicio != None:
			self.inicio = self.inicio.proximo
			self.tamanho -= 1
		self.imprimir()

	def removerDoFim(self): 
		if self.inicio == None:
			print("Lista Vazia")
		elif self.inicio.proximo == None:
			self.inicio = None
			self.tamanho = 0
		else:
			anterior = self.inicio
			aux = self.inicio.proximo
			while aux.proximo:
				anterior = aux
				aux = aux.proximo
			anterior.proximo = None
			self.tamanho -= 1
		self.imprimir()


	


		

			
