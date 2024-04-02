from Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, marca, ano, cat, qtdPortas):
        super().__init__( marca, ano, cat )
        self.qtdPortas = qtdPortas

    def __str__(self):
        texto = super().__str__()
        texto += "Portas: " + str( self.qtdPortas )
        return texto
        # return super().__str__() + "Portas: " + str( self.qtdPortas )

    def imprimir(self):
        super().imprimir()
        print( "Portas: " + str( self.qtdPortas ) )
        


