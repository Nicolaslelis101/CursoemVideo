def maior(* num):
    maior = 0
    cont = 0
    for valor in num:
        print(f"{valor}", end=" ")
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"\nMaior número: {maior}")


maior(2, 5, 6, 4, 8)
