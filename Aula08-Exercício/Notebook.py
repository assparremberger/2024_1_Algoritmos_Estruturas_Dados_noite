from Computador import Computador

class Notebook(Computador):

    def __init__(self, modelo, ano, preco, tempodebateria):
        super().__init__(modelo, ano, preco)
        self.__tempoDeBateria = tempodebateria
    
    
    def cadastrar(self):
        print("Notebook cadastrado")
        


    def getInformacoes(self):
        return super().getInformacoes() + f" , {self.__tempoDeBateria}"
    

