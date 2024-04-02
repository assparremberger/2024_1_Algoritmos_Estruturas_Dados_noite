from Aluno import Aluno
class AlunoGraduacao(Aluno):
    def __init__(self, id, name, matricula, semestre):
        super().__init__(id, name, matricula)
        self.semestre = semestre
    
    def imprimir(self):
        print("Código: " , self.codigo)
        print("Nome: " , self.nome)
        print("Matrícula: " , self.matricula)
        print("Semestre: " , self.semestre )
        
