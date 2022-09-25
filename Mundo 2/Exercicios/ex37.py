num = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para converter:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal""")
while True:
    opcao = int(input("Sua opção: "))
    if opcao == 1:
        print(f"{num} para binário é: {bin(num)[2:]}")
        break
    elif opcao == 2:
        print(f"{num} para octal é: {oct(num)[2:]}")
        break
    elif opcao == 3:
        print(f"{num} para hexadecimal é: {hex(num)[2:]}")
        break
    else:
        print("Digite os números listados a cima!")
