from Livro import Livro
from Pilha import Pilha

l1 = Livro("O tempo e o Vento", "Érico Veríssimo")
l2 = Livro("Dom Casmurro", "Machado de Assis")
l3 = Livro("Senhor dos Anéis", "Tolkien")
l4 = Livro("Guerra dos Tronos", "George Martins")

pilha = Pilha()
pilha.imprimir()

pilha.add(l1)
pilha.add(l2)
pilha.add(l3)
pilha.remover()
pilha.add(l4)
pilha.remover()
pilha.remover()
pilha.remover()
pilha.remover()


