soma_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulher_20 = 0
for p in range(1, 4+1):
    print(f"---{p}---Pessoa")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper().strip()
    soma_idade += idade
    if p == 1 and sexo == "M":
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in "M" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in "F" and idade < 20:
        total_mulher_20 += 1
media_idade = soma_idade / 4
print(f"A média de idade do grupo é: {media_idade}.")
print(f"O homem mais velho é {nome_velho} e tem {maior_idade_homem} anos.")
print(f"O total de mulheres com menos de 20: {total_mulher_20}.")
