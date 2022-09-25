exp = input("Digite a expressão: ")
lista = list()
for simbolo in exp:
    if simbolo == "(":
        lista.append("(")
    elif simbolo == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break
if len(lista) == 0:
    print("Sua expressão é válida!")
else:
    print("A expressão está errada!")
