from random import choice
alunos = []
for i in range(4):
    aluno = input(f"Digite o nome do {i+1} aluno: ")
    alunos.append(aluno)
escolhido = choice(alunos)
print(f"O aluno escolhido foi: {escolhido}")
