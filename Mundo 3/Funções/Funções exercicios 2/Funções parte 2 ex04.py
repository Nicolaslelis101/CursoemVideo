def leiaInt(num):
    valor = 0
    while True:
        n = input(num)
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print("Digite um número inteiro.")
    return valor


n = leiaInt("Digite um número: ")
print(f"Número digitado: {n}")
