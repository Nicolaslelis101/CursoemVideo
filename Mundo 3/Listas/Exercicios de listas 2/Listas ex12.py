ficha = []
while True:
    nome = input("Nome: ")
    nota1 = float(input("Nota1: "))
    nota2 = float(input("Nota2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = input("Quer continuar? [S/N] ").upper().strip()
    if resposta in "N":
        break
print('-='*30)
print(f"{'no.':<4}{'NOME':<10}{'MEDIA':>8}")
print('-='*30)
for i, a in enumerate(ficha):
    print(f"{i+1:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print('-='*30)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe)"))
    if opc == 999:
        print("FINALIZANDO....")
        break
    if opc <= len(ficha):
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")
print("<<< VOLTE SEMPRE >>>")
