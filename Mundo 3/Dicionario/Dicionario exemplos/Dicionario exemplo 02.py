brasil = []
estado = {}
for c in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do estado: "))
    brasil.append(estado.copy())
for e in brasil:
    for c, v in e.values():
        print(f"O campo{c} tem o valor: {v}", end=' ')
    print()
