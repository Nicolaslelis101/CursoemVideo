from random import randint


def sorteia(num):
    print("Números aleatórios: ")
    for cont in range(5):
        num.append(randint(1, 10))
    print(num, end=" ")


def somaPar(num):
    soma = 0
    for valor in num:
        if valor % 2 == 0:
            soma += valor
    print(f"\nSoma de todos os valores pares: {soma}")


numeros = []
sorteia(numeros)
somaPar(numeros)
