n1 = int(input("Digite o primeiro elemento: "))
n2 = int(input("Digite o segundo elemento: "))
opcao = 0
while opcao != 5:
    print("""
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa""")
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        soma = n1 + n2
        print(f"Soma {soma}")
    elif opcao == 2:
        multi = n1 * n2
        print(f"Multiplicação {multi}")
    elif opcao == 3:
        if n1 < n2:
            maior = n1
        else:
            maior = n2
        print(f"O maior é: {maior}")
    elif opcao == 4:
        n1 = int(input("Digite o primeiro elemento: "))
        n2 = int(input("Digite o segundo elemento: "))
    elif opcao == 5:
        print("Fim do programa.")
        break
    else:
        print("Número inválido, Digite novamente.")
