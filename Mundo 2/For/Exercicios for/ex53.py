frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
# inverso = junto[::-1] se não quiser usar o for....
if inverso == junto:
    print("É palindromo!")
else:
    print("Não é um palindromo!")
