alunos = {}

for valor in range(1,4):
    nome = input(f"\nDigite o nome do aluno {valor}: ")
    nota = float (input(f"Digite a nota do aluno {valor}: "))
    alunos[nome] = nota

somaNotas = 0
for nota in alunos.values():
    somaNotas += nota

mediaNotas = somaNotas / len(alunos)

print("Média das notas dos alunos:")
for nome, nota in alunos.items():
    print("{}: {:.2f}".format(nome, nota))

print("Média geral: {:.2f}\n".format(mediaNotas))
