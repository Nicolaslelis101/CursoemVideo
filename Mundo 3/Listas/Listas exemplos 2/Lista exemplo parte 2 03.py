galera = []
dados = []
menor = maior = 0
for i in range(3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    galera.append(dados[:])
    dados.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade!")
        maior += 1
    else:
        print(f"{p[0]} è menor de idade!")
        menor += 1
print(f"Temos {maior} de maiores e {menor} de menores.")

