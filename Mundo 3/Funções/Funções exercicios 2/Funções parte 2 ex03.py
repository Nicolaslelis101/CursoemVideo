def ficha(n=" ", g=0):
    print(f"Jogador {n} || Gols {g}")


nome = input("Nome do jogador: ")
gols = input("Gols: ")
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == " ":
    ficha(g=gols)
else:
    ficha(nome, gols)
