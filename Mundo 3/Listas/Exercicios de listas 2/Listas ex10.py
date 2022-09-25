num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = 0
maior = 0
scol = 0
for i in range(3):
    for j in range(3):
        num[i][j] = int(input("Digite um número: "))
for i in range(3):
    for j in range(3):
        print(f"[{num[i][j]:^5}]", end='')
        if num[i][j] % 2 == 0:
            spar += num[i][j]
    print()
for l in range(3):
    scol += num[l][2]
    if l == 0:
        maior = num[1][l]
    elif num[1][l] > maior:
        maior = num[1][l]
print(f"A soma dos números pares é {spar}")
print(f"A soma da terceira coluna é {scol}")
print(f"O maior número da segunda linha é {maior}")


