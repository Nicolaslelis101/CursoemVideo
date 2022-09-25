distancia = float(input("Digite a distancia percorrida em Km: "))
if distancia >= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print(f"Você vai pagar: {preco} ")
