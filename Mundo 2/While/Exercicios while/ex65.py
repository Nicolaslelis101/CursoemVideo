resp = 'S'
soma = 0
quant = 0
media = 0
maior = 0
menor = 0

while resp == 'S':
    n = int(input("Digite um número: "))
    soma += n
    quant += 1
    if quant == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = input("Quer continuar? [S/N] ").upper().strip()
media = soma / quant
print(f"Você digitou {quant} números e a média deu {media}. Maior: {maior} e menor: {menor}.")
