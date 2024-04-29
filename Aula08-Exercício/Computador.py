from abc import ABC, abstractmethod

class Computador(ABC):
    def __init__(self,modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    @abstractmethod
    def cadastrar(self):
        pass

    def getInformacoes(self):
        texto = f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: {self.preco}"
        return texto

    