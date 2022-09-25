from random import randint
itens = ("\033[31m pedra \033[m", "\033[32m papel \033[m", "\033[33m tesoura \033[m")
computador = randint(0, 2)
print("""Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input("Qual sua ecolha: "))
print("="*10)
print(f"O computador escolheu: {itens[computador]}")
print(f"O jogador jogou: {itens[jogador]}")
print("="*10)
if computador == 0:
    if jogador == 0:
        print(f"EMPATE")
    elif jogador == 1:
        print(f"\033[32m VOCE VENCEU \033[m")
    elif jogador == 2:
        print(f"\033[31m COMPUTADOR VENCEU \033[m")

elif computador == 1:
    if jogador == 0:
        print(f"\033[31m COMPUTADOR VENCEU \033[m")
    elif jogador == 1:
        print(f"EMPATE")
    elif jogador == 2:
        print(f"\033[32m VOCE VENCEU \033[m")

elif computador == 2:
    if jogador == 0:
        print(f"\033[32m VOCE VENCEU \033[m")
    elif jogador == 1:
        print(f"\033[31m COMPUTADOR VENCEU \033[m")
    elif jogador == 2:
        print(f"EMPATE")
