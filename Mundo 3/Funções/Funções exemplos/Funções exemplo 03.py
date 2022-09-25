def dobra(val):
    pos = 0
    while pos < len(val):
        val[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
print(f"Normal: {valores}")
dobra(valores)
print(f"Dobro: {valores}")
