class Estudante:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e estou cursando {self.curso}."

aluno1 = Estudante("Charles", 20, "Desenvolvedor")
aluno2 = Estudante("Suel", 19, "Desenvolvedor")
aluno3 = Estudante("Julio", 21, "Engenharia")

print(aluno1.apresentar())
print(aluno2.apresentar())
print(aluno3.apresentar())
