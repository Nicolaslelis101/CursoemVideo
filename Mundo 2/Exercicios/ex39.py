atual = int(input("Digite o ano atual: "))
nasc = int(input("Digite o ano do seu nascimento: "))
idade = atual - nasc
print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}")
if idade == 18:
    print("Tem que se alistar IMEDIATAMENTE")
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f"Ainda faltam {saldo} anos. Seu alistamento será em {ano}!")
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f"Deeveria ter se alistado a {saldo} anos. Seu alistamento foi em {ano}!")
