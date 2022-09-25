from lib.interface import *
from lib.arquivo import *

arq = 'CURSOEMVIDEO.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

cabecalho("SISTEMA ARQUIVO v1.0")
resposta = menu(['Ver Pessoas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
while True:
    if resposta == 1:
        lerArquivo(arq)
        break
    elif resposta == 2:
        cabecalho("Novo cadastro")
        nome = str(input("Nome: "))
        idade = LeiaInt("idade: ")
        cadastrar(arq, nome, idade, )
        break
    elif resposta == 3:
        cabecalho("\033[32mFinalizando o sistema...\033[m")
        break
    else:
        print("\033[31mOpção invalida.\033[m")
