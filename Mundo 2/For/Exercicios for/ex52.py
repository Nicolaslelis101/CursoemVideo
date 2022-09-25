num = int(input("Digite um valor: "))
total = 0
for i in range(1, num+1):
    if num % i == 0:
        print("\033[34m", end="")
        total += 1
    else:
        print("\033[31m", end="")
    print(f"{i}", end="")
print(f"\n O número {num} foi dividido {total}")
if total == 2:
    print("É primo!")
else:
    print("Não é primo!")
