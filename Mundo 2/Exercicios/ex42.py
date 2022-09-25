r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("Pode se formar o trinagulo:", end="")
    if r1 == r2 == r3:
        print("Equilátero.")
    elif r1 != r2 != r3:
        print("Escaleno.")
    else:
        print("Isóceles")
else:
    print("Não forma triangulo.")
