soma = 0
cont = 0
while True:
    num = int(input("Digite um número [999 para parar]: "))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print(f"Soma: {soma}. Qauntidade de valores {cont}.")

