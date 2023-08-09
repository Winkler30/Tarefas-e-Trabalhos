class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
aluno1 = Estudante("Charles", 20)
aluno2 = Estudante("Suel", 19)
aluno3 = Estudante("Julio", 21)

print(aluno1.apresentar())
print(aluno2.apresentar())
print(aluno3.apresentar())
