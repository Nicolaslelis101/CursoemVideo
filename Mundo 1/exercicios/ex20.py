from random import shuffle
alunos = []
for i in range(4):
    aluno = input(f"Digite o nome do {i+1} aluno: ")
    alunos.append(aluno)
shuffle(alunos)
print(f"A ordem é: {alunos}")
