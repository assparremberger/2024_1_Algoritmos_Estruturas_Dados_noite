class Categoria:

    def __init__(self, id = 0, nome = "Outra"):
        self.id = id
        self.nome = nome

    def __str__(self):
        return "Categoria: " + self.nome