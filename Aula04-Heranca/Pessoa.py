class Pessoa:

    def __init__(self, name = "Daniel", phone = "(51) 12345"):
        self.nome = name
        self.fone = phone

    def __str__(self):
        text = "Nome: " + self.nome + "\n"
        text += "Fone: " + self.fone + "\n"
        return text
    def imprimir(self):
        print( self )