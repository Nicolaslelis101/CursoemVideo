from datetime import date
atual = date.today().year
nascimento = int(input("Degite seu ano de nascimento: "))
idade = atual - nascimento
print(f"O atleta tem {idade} anos.")
if idade <= 9:
    print("CLASSIFICAÇÃO: MIRIM")
elif idade <= 14:
    print("CLASSIFICAÇÃO: INFANTIL")
elif idade <= 19:
    print("CLASSIFICAÇÃO: JUNIOR")
elif idade <= 25:
    print("CLASSIFICAÇÃO: SÊNIOR")
else:
    print("CLASSIFICAÇÃO: MASTER")
