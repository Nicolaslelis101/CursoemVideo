from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(n)
print("Os números sorteados foram: ", end="")
for i in n:
    print(f"{i} ", end="")
print(f"\nMaior valor: {max(n)}")
print(f"Menor valor: {min(n)}")
