class Conta:

    tarifa = 1.99
    logado = True

    def __init__(self):
        self.__saldo = 0

    def getSaldo(self):
        if self.logado: 
            return self.__saldo
        else:
            print("Ação não pertida")
            return None

    def setSaldo(self, valor):
        if self.logado and valor >= 0:
            self.__saldo = valor
        else:
            print("Ação não pertida")

    @property
    def saldo(self):
        if self.logado: 
            return self.__saldo
        else:
            print("Ação não pertida_")
            return None

    @saldo.setter
    def saldo(self, valor):
        if self.logado and valor >= 0:
            self.__saldo = valor
        else:
            print("Ação não pertida")

    def __descontarTarifa(self):
        self.__saldo -= self.tarifa

    def depositar(self, valor):
        if self.__saldo + valor >= self.tarifa:
            self.__saldo += valor
            self.__descontarTarifa() 
        else:
            print("Saldo Insuficiente!")
    
    def sacar(self, valor):
        if self.__saldo - valor >= self.tarifa:
            self.__saldo -= valor
            self.__descontarTarifa() 
        else:
            print("Saldo Insuficiente!")


