num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        num[i][j] = int(input("Digite um número: "))
for i in range(3):
    for j in range(3):
        print(f"[{num[i][j]:^5}]", end='')
    print()

