from random import randint
cont = 0
while True:
    jogador = int(input("Digite um número par ou ímpar: "))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input("Par ou ímpar? [P/I] ")).upper().strip()
    if tipo == "P":
        if total % 2 == 0:
            print(f"Você ganhou. Jogador: {jogador} + computador: {computador} = {total}")
            cont += 1
        else:
            print(f"Você Perdeu. Jogador: {jogador} + computador: {computador} = {total}")
            break
    elif tipo == "I":
        if total % 2 == 0:
            print(f"Você  Perdeu. Jogador: {jogador} + computador: {computador} = {total}")
            break
        else:
            print(f"Você Ganhou. Jogador: {jogador} + computador: {computador} = {total}")
            cont += 1
print(f"Total de tentativas = {cont}.")
