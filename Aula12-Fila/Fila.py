from No import No

class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo  
        else:
            self.fim.proximo = nodo
        self.fim = nodo
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        print( "-----------------------------------" )
        if self.inicio == None:
            print( "Fila vazia" )
        else:
            print("Fila com ", self.tamanho, " elementos")
            aux = self.inicio
            texto = ""
            while aux:
                texto += aux.dado  + " - "
                aux = aux.proximo
            print(texto)

    # def remover(self):
    #     if self.inicio:
    #         if self.inicio.proximo == None:
    #             self.inicio = None
    #             self.fim = None
    #         else:
    #             self.inicio = self.inicio.proximo
    #         self.tamanho -= 1
    #     self.imprimir()

    def remover(self):
        if self.inicio:
            self.inicio = self.inicio.proximo
            if self.inicio == None:
                self.fim = None
            self.tamanho -= 1
        self.imprimir()
            





    