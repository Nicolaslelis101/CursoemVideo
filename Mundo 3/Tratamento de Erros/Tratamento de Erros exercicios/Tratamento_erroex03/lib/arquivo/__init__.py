def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("ERRO MA CRIAÇÃO DO ARQUIVO")
    else:
        print("Arquivo criado com sucesso!")


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("ERRO AO LER O ARQUIVO!!!")
    else:
        print('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("ERRO NA ABERTURA DO ARQUIVO")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("OUVE UM ERRO NA ESCRITA DO ARQUIVO.")
        else:
            print(f"Novo registro {nome} adicionado.")
            a.close()
