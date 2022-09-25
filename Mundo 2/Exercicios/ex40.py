nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2
if 7 > media >= 5:
    print("Recuperação.")
elif media < 5:
    print("Reprovado.")
else:
    print("aprovado.")
