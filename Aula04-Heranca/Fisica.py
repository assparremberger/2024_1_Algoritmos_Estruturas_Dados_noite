from Pessoa import Pessoa
class Fisica(Pessoa):

    def __init__(self, nome, telefone, cpf):
        super().__init__(self, nome, telefone)
        self.cpf = cpf
        print("Física criada")
