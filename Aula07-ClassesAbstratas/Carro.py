from Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, modelo, ano, nPortas):
        super().__init__(modelo, ano)
        self.qtdPortas = nPortas

    def ligar(self, chave):
        if chave == "1234" :
            print("Carro ligado")
        else: 
            print("Não foi possível ligar o Carro")

    def imprimir(self):
        super().imprimir()
        print("Quantidade de Portas: " , self.qtdPortas)

    