casa = float(input("Valr da casa R$: "))
salario = float(input("Salario do comprador: "))
anos = int(input("Quantos anos o financiamento: "))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f"Para pagar uma casa de {casa:.2f}R$ em {anos} a prestação será de {prestacao:.2f}R$")
if prestacao <= minimo:
    print("Emprétimo pode ser concedido.")
else:
    print("Empréstimo negado.")
