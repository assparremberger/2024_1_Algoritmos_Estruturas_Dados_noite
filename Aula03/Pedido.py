from Produto import Produto
from Pessoa import Pessoa
class Pedido:
    def __init__(self, end, cliente = Pessoa("Anônimo") ):
        self.id = None
        self.end = end
        self.cliente = cliente
        self.produtos = []
    def addProduto(self , prod ):
        self.produtos.append( prod )
        soma = 0 
        for p in self.produtos:
            soma += p.preco
        return soma

    def __str__(self):
        texto = "Endereço do Pedido: " + self.end + " - " + self.cliente.cidade.nome
        texto += "\n Cliente: " + self.cliente.nome
        texto += "\nProdutos: \n"
        if len( self.produtos ) == 0:
            texto += "Pedido Vazio"
        for p in self.produtos:
            texto += p.nome+" - "+str( p.preco )+ " - Cat: " + p.cat.nome +"\n"
        return texto


    