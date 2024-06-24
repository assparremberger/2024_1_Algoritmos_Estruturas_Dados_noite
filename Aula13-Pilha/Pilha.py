from Livro import Livro
class Pilha:
    def __init__(self):
        self.top = None
        self.tamanho = 0

    def add( self, objLivro):
        if self.top != None:
            objLivro.proximo = self.top
        self.top = objLivro
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        aux = self.top
        while( aux ):
           print( aux ) 
           aux = aux.proximo
        print( "Total: " , self.tamanho )

    def remover(self):
        if self.top == None:
            print("Pilha Vazia")
        else:
            self.top = self.top.proximo
            self.tamanho -= 1
            self.imprimir()
