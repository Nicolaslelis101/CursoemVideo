cor = ("\033[m", #0 - Sem cores
       "\033[0;30;41m", #1- Vermelho
       "\033[0;30;42m", #2 - verde
       "\033[0;30;43m", #3 - Amarelo
       "\033[0;30;44m", #4 - Amarelo
       "\033[0;30;45m", #5 - Roxo
       "\033[7;30m" #6 - Branco
      )


def ajuda(c):
    titulo(f"Acessando o manual do comando \'{c}\'", 4)
    print(cor[2], end='')
    help(c)
    print(cor[0], end='')

def titulo(msg, color=0):
    tam = len(msg) + 4
    print(cor[color], end='')
    print("-"*tam)
    print(f"{msg}")
    print("-"*tam)
    print(cor[0], end='')

comando = ''
while True:
    comando = input("Função da biblioteca: ")
    if comando.upper() == 'FIM':
        titulo("Até logo.", 1)
        break
    else:
        ajuda(comando)

