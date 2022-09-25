soma = 0
cont = 0
for i in range(1, 6+1):
    num = int(input("Digite um valor: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"Você informou {cont} núneros e a soma deu {soma}")
