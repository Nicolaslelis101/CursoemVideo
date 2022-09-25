total = 0
total_mil = 0
menor = 0
cont = 0
barato = " "
while True:
    produto = input("Nome do produto: ")
    preco = float(input("Preço: "))
    cont += 1
    total += preco
    if preco > 1000:
        total_mil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = " "
    while resp not in "SN":
        resp = input("Quer continuar? ").strip().upper()
    if resp == "N":
        break
print(f"Produtos com mais de mil: {total_mil}. Produtos baratos -> Nome: {barato} preço: {menor}.")

