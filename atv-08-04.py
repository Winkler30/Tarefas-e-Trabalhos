class Estudante:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e estou cursando {self.curso}."

    def aniversario(self):
        self.idade += 1

aluno = Estudante("Charles", 20, "Desenvoldedor")

aluno.aniversario()

print(aluno.apresentar())
