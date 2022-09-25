from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for pessoa in range(1, 7+1):
    nascimento = int(f"Digite o ano do nascimento da {pessoa} pessoa: ")
    idade = atual - nascimento
    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print(f"O total de menor de idade são: {total_menor}")
print(f"O total de maior de idade são: {total_maior}")
