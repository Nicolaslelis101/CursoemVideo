lista = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
    else:
        print("Número ja digitado!!!!!")
    r = str(input("Deseja continuar ? [S/N] ")).upper().strip()
    while True:
        if r not in "SN":
            print("DIGITE S OU N")
            r = str(input("Deseja continuar ? [S/N] ")).upper().strip()
        else:
            break
    if r == "N":
        break
lista.sort()
print(lista)
