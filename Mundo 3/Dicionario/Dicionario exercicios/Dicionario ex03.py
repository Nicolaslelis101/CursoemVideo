from datetime import datetime
dados = {}
dados['Nome:'] = str(input("Nome: "))
nascimento = int(input("Ano de nascimento: "))
dados['Idade:'] = datetime.now().year - nascimento
dados['Ctps:'] = int(input("Carteira de Trabalho (0 não tem): "))
if dados['Ctps:'] != 0:
    dados['Contratação:'] = int(input("Ano de contratação: "))
    dados['Salário:'] = float(input("Salário: "))
    dados['Aposentadoria:'] = dados['Idade:'] + ((dados['Contratação:'] + 35) - datetime.now().year)
else:
     del dados['Ctps:']

for c, v in dados.items():
    print(f"- {c} {v}")




