from abc import ABC, abstractmethod
# class Veiculo(metaclass=ABCMeta)
class Veiculo(ABC):

    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    @abstractmethod
    def ligar(self, chave):
        pass

    def imprimir(self):
        print("Modelo: ", self.modelo)
        print("Ano: ", self.ano)

    def desligar(self):
        print("Veículo desligado")

