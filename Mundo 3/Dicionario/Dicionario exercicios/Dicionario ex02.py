from random import randint
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}


for chave, valor in jogadores.items():
    print(f"{chave}: Face do dado -> {valor}")
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"{i+1} lugar: {v[0]} com {v[1]}")
