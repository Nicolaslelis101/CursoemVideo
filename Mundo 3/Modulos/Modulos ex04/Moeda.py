def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxa=0):
    print(f"Preço: {moeda(preco)}"
          f"\nAumento de taxa: {aumentar(preco, taxa, True)}"
          f"\nRedução de taxa: {diminuir(preco, taxa, True)}"
          f"\nDobro: {dobro(preco, True)}"
          f"\nMetade: {metade(preco, True)}")
