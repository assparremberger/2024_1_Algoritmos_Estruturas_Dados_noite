from Computador import Computador


class Desktop(Computador): 
    def __init__(self,  modelo, cor, preco, potenciaDaFonte):
    
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte


    def cadastrar(self):
        print("Desktop cadastrado")
          


    def getInformacoes(self):
        return super().getInformacoes() +", " + self._potenciaDaFonte

