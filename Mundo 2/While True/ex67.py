while True:
    num = int(input("Digite um número para ver a tabuada: "))
    for c in range(1, 10+1):
        print(f"{c} X {num} = {c*num}")
    while True:
        pergunta = input("Deseja continuar?[S/N] ").upper().strip()
        if pergunta not in "SN":
            print("Digite S ou N.")
        else:
            break
    if pergunta == "N":
        break
