salario = float(input("Digite seu salario: "))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print(f"Seu novo salario é: {novo}")
else:
    novo = salario + (salario * 10 / 100)
print(f"Seu novo salario é: {novo}")
