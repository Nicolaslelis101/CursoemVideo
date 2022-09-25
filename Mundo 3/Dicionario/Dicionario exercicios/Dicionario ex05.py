pessoas = list()
pessoa = dict()
soma = 0
media = 0
while True:
    pessoa.clear()
    pessoa['Nome:'] = str(input("Digite seu nome: "))
    while True:
        pessoa['Sexo:'] = str(input("Sexo: [M/F] ")).upper()[0]
        if pessoa['Sexo:'] in "MF":
            break
        else:
            print("Digite M ou F, por favor!")
    pessoa['Idade:'] = int(input("Digite a idade: "))
    soma += pessoa['Idade:']
    pessoas.append(pessoa.copy())
    while True:
        resposta = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resposta not in "SN":
            print("Digite S ou N, por favor!")
        else:
            break
    if resposta == "N":
        break
print(pessoas)
print(f"Ao todo temos {len(pessoas)} pessoas cadastradas.")
media = soma / len(pessoas)
print(f"A média de idade é de {media:5.2f} anos.")
print(f"As mulheres cadastradas foram ", end="")
for i in pessoas:
    if i['Sexo:'] in "F":
        print(f"{i['Nome:']} ", end=" ")
print()
print(f"Lista das pessoas acima da média: ")
for i in pessoas:
    if i['Idade:'] >= media:
        for c, v in i.items():
            print(f"{c} {v}")
        print()
