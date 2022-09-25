def contador(i, f, p):
    cont = i
    if i < f:
        for i in range(i, f+1, p):
            print(cont, end=" ")
            cont += p
        print()
    else:
        for i in range(f, i+1, p):
            print(cont, end=" ")
            cont -= p
        print()


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input("Digite o inicio da contagem: "))
fim = int(input("Digite o fim da contagem: "))
passo = int(input("Digite o passo da contagem: "))
contador(inicio, fim, passo)
