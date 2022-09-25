cont = 0
soma = 0
num = int(input("Digite um número [999 para parar.]: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um número [999 para parar.]: "))
print(f"Acabou. Você digitou {cont} números e sua soma é: {soma}.")
