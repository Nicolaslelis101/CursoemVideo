jogador = dict()
partidas_lista = list()
jogador['Nome:'] = str(input("Nome: "))
partidas = int(input(f"Quantidades de partidas do {jogador['Nome:']}: "))
for c in range(0, partidas):
    partidas_lista.append(int(input(f"Quantidades de gols na partida {c+1}: ")))
jogador['Gols:'] = partidas_lista[:]
jogador['Total de gols:'] = sum(partidas_lista)
for c, v in jogador.items():
    print(f"{c} {v}")

