from datetime import date


def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return "Não vota"
    elif 16 <= idade < 18 or idade > 65:
        return "Voto opcional"
    else:
        return "Voto obrigatório"


nasc = int(input("Em que ano você nasceu: "))
print(voto(nasc))
