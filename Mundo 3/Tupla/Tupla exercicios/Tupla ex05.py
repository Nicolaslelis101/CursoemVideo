lista_produtos = ("Lápis", 1.75,
                  "Borracha", 2,
                  "Caderno", 15.90,
                  "Estojo", 25)
print("----PRODUTOS----")
for pos in range(0, len(lista_produtos)):
    if pos % 2 == 0:
        print(f"{lista_produtos[pos]} ", end="")
    else:
        print(f"R${lista_produtos[pos]}")
