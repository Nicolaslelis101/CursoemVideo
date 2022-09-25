lista = []
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    r = input("Quer continuar ? [S/N] ").upper().strip()
    while True:
        if r not in "SN":
            print("DIGITE S OU N...")
            r = input("Quer continuar ? [S/N] ").upper().strip()
        else:
            break
    if r == 'N':
        break
lista.sort(reverse=True)
print(f"Foram digitados {len(lista)} números")
print(f"Lista em decrescente {lista}")
if 5 in lista:
    print("O número 5 esta na lista.")
else:
    print("O número 5 não se encontra na lista")
