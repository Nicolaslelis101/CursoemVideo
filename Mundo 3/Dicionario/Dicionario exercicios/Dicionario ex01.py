aluno = dict()
aluno['Nome:'] = str(input("Nome: "))
aluno['Média:'] = float(input(f"Média do {aluno['Nome:']}: "))
if aluno['Média:'] >= 7:
    aluno['Situação:'] = "Aprovado"
elif 5 <= aluno['Média:']:
    aluno['Situação:'] = "Recuperação"
else:
    aluno['Situação:'] = "Reprovado"
for chave, valor in aluno.items():
    print(f"{chave} {valor}")
