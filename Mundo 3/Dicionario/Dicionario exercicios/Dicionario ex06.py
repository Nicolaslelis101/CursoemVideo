time = list()
jogador = dict()
partidas_lista = list()
while True:
    jogador.clear()
    jogador['Nome:'] = str(input("Nome: "))
    partida = int(input(f"Quantidades de partidas do {jogador['Nome:']}: "))
    partidas_lista.clear()
    for c in range(0, partida):
        partidas_lista.append(int(input(f"Quantidades de gols na partida {c+1}: ")))
    jogador['Gols:'] = partidas_lista[:]
    jogador['Total de gols:'] = sum(partidas_lista)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in 'SN':
            break
        else:
            print("Digite novamente.")
    if resp == "N":
        break
print("Num ", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("-"*30)
for k, v in enumerate(time):
    print(f"{k:>3}", end="")
    for d in v.values():
        print(f"{str(d):>15}", end="")
    print()
print("-"*30)
print(f"O jogador {jogador['Nome:']} jogou {len(jogador['Gols:'])} partidas")
for i, v in enumerate(jogador['Gols:']):
    print(f"    => Na partida {i+1}, fez {v} gols.")
print(f"Foi um total de {jogador['Total de gols:']} gols.")
while True:
    busca = int(input("Mostrar dados do jogador ? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"Não existe esse jofador do código {busca}")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {time[busca]['Nome:']}")
        for i, g in enumerate(time[busca]['Gols:']):
            print(f"   No jogo {i+1} fez {g} gols.")
        print("-"*30)
print("Volte sempre.")
