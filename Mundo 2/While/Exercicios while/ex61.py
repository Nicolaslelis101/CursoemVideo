num = int(input("Primeiro termo: "))
razao = int(input("Razâo: "))
decimo = num + (10 - 1) * razao
termo = num
cont = 1
while cont <= 10:
    print(f"{termo} ->", end=" ")
    termo += razao
    cont += 1
print("Acabou.")