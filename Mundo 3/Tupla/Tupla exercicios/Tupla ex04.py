n = (int(input("Digite um número: ")),
     int(input("Digite um número: ")),
     int(input("Digite um número: ")),
     int(input("Digite um número: ")))
print(f"Você digitou {n}")
print(f"Quantos 9s: {n.count(9)}")
print(f"Posição do número 3: {n.index(3)}")
print(f"Números pares: ", end="")
for i in n:
    if i % 2 == 0:
        print(f"{i} ", end="")

