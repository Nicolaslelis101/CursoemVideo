dados = []
total = []
pesado = leve = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Peso: ")))
    if len(total) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    total.append(dados[:])
    dados.clear()
    pergunta = input("Quer continuar ? [S/N] ").upper().strip()
    if pergunta == "N":
        break
print(f"Os dados foram {total}")
print(f"Pessoas listadas {len(total)}")
print(f"O maior peso foi {pesado}Kg de ", end='')
for peso in total:
    if peso[1] == pesado:
        print(peso[0])
print(f"O menor peso {leve}Kg foi de ", end='')
for peso in total:
    if peso[1] == leve:
        print(peso[0])
