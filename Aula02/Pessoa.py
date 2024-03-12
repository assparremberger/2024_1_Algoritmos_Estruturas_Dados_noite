class Pessoa:

    def __init__(self, nome, idade=18):
        self.nome = nome
        self.idade = idade
        print( "Pessoa " , self.nome, " construída")