from random import randint
computador = randint(0, 5)
n = int(input("Advinhe o número: "))
if n == computador:
    print("Parabens")
else:
    print(f"Você errou! Era o número {computador}")
