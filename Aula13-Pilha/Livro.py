class Livro:

    def __init__(self, titulo, autor ):
        self.titulo = titulo
        self.autor = autor
        self.proximo = None
        
    def __str__(self):
        return self.titulo + " - " + self.autor 