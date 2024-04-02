from Aluno import Aluno
class AlunoEnsinoMedio(Aluno):
    def __init__(self, id, name, matricula, year):
        super().__init__(id, name, matricula)
        self.ano = year
    
    def imprimir(self):
        print("Código: " , self.codigo)
        print("Nome: " , self.nome)
        print("Matrícula: " , self.matricula)
        print("Ano: " , self.ano )
        
