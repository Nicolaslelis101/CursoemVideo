palavras = ("Aprender", "Programar", "Programar", "Python")
for p in palavras:
    print(f"\nNa letra {p} temos ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")

