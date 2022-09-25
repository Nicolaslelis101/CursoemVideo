def par(n):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input("Digite um número: "))
if par(num):
    print("Par")
else:
    print("Não é par")
