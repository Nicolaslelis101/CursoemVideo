sexo = input("Informe o sexo [M/F]: ").upper().strip()[0]
while sexo not in 'MF':
    sexo = input("Dados inválidos. Informe o sexo [M/F]: ").upper().strip()[0]
print(f"Seu sexo é: {sexo}")
