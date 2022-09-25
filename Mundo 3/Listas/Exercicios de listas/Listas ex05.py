lista = []
lista_par = []
lista_impar = []

while True:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    lista.append(num)
    p = input("Quer continuar ? [S/N] ").upper().strip()
    while True:
        if p not in "SN":
            print("DIGITE S OU N...")
            p = input("Quer continuar ? [S/N] ").upper().strip()
        else:
            break
    if p == "N":
        print("Obrigado.")
        break
print(f"Lista com números pares {lista_par}")
print(f"Lista com números impares {lista_impar}")
print(f"Lista com todos os números {lista}")
