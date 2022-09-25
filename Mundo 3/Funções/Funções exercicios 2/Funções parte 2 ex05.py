def notas(*n, sit=False):
    r = dict()
    r['Total:'] = len(n)
    r['Maior:'] = max(n)
    r['Menor:'] = min(n)
    r['Média:'] = sum(n)/len(n)
    if sit:
        if r['Média:'] >= 7:
            r['Situação:'] = "Boa"
        elif r['Média:'] >= 5:
            r['Situação:'] = "Razoavel"
        else:
            r['Situação:'] = "Ruim"
    return r


nota = notas(5.5, 2.5, 9, 8.5, sit=True)
print(nota)
