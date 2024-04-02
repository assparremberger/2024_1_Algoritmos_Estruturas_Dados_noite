from Categoria import Categoria

class Veiculo:
    def __init__(self, marca = "Honda" , ano = 2014 , cat = Categoria( None ) ):
        self.id  = None
        self.marca = marca
        self.ano = ano
        self.categoria = cat

    def __str__(self):
        texto = "Marca: " + self.marca + "\n"
        texto += "Ano: "  + str(self.ano) + "\n"
        texto += "Categoria: "  + str(self.categoria.nome) + "\n"
        return texto

    def imprimir(self):
        print( "Veiculo: \n" , self )
        # print( "Veiculo: \n" , self.__str__() )
        # print( "Veiculo: \n" , str( self ) )