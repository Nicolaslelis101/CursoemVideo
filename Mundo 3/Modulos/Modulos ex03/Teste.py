import Moeda

p = float(input("Digite o preço: "))
t = float(input("Digite a taxa: "))
print(f"Preço: {Moeda.moeda(p)}"
      f"\nAumento: {Moeda.aumentar(p, t, True)}"
      f"\nRedução: {Moeda.diminuir(p, t, True)}"
      f"\nDobro: {Moeda.dobro(p, True)}"
      f"\nMetade: {Moeda.metade(p, True)}")

