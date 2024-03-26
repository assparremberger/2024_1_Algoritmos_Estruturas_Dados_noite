from Categoria import Categoria
class Produto:
    def __init__(self, nome, preco=10.0, qtd = 0, cat=Categoria( None ) ):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.cat = cat
    def __str__(self):
        texto = "Produto: " + self.nome 
        texto += "\nPreço: " + str( self.preco) 
        texto += "\nCategoria: " + self.cat.nome 
        return texto



