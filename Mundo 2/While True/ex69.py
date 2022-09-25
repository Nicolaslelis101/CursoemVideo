tot18 = 0
toth = 0
totm20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = input("Sexo: ").strip().upper()
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        toth += 1
    if sexo == "F" and idade < 20:
        totm20 += 1
    resp = " "
    while resp not in "SN":
        resp = input("Quer continuar? ").strip().upper()
    if resp == "N":
        break
print(f"Pesoas com 18: {tot18}. Homens: {toth}. Mulheres com mais de 20 anos: {totm20}.")

