from random import randint
computador = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Advinhe o número entre 1 e 10: "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print("Digitou um pouco a mais, tenta de novo.")
        elif jogador < computador:
            print("Digitou um pouco a menos, tenta de novo.")
print(f"Parabéns! Você acertou na {palpites} tentativa.")
