num = int(input("Primeiro termo: "))
razao = int(input("Razâo: "))
termo = num
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} ->", end=" ")
        termo += razao
        cont += 1
    print("Acabou.")
    mais = int(input("Você quer mais algum termo? "))
print(f"termos mostrados: {total}")
