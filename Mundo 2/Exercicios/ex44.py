preco = float(input("Preço das compras: R$"))
print("""Formas de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
while True:
    opcao = int(input("Qual sua escolha? "))
    if opcao == 1:
        total = preco - (preco * 10 / 100)
        print(f"Sua compra de {preco:.2f}R$ vai custar {total:.2f}R$ no final ")
        break
    elif opcao == 2:
        total = preco - (preco * 5 / 100)
        print(f"Sua compra de {preco:.2f}R$ vai custar {total:.2f}R$ no final ")
        break
    elif opcao == 3:
        total = preco
        parcela = total / 2
        print(f"O produto será parcelado em 2x de {parcela} SEM JUROS")
        print(f"Sua compra de {preco:.2f}R$ vai custar {total:.2f}R$ no final ")
        break
    elif opcao == 4:
        total = preco + (preco * 20 / 100)
        total_parcela = int(input("Quantas vezes você quer parcelar? "))
        parcela = preco / total_parcela
        print(f"O produto será parcelado em {total_parcela}x de {parcela:.2f} COM JUROS ")
        print(f"Sua compra de {preco:.2f}R$ vai custar {total:.2f}R$ no final ")
        break
    else:
        total = preco
        print(f"ERRO! OPÇÃO INVÁLIDA!")
