import Moeda

p = float(input("Digite o preço: "))
t = float(input("Digite a taxa: "))
print(f"Preço: {Moeda.moeda(p)}"
      f"\nAumento: {Moeda.moeda(Moeda.aumentar(p, t))}"
      f"\nRedução: {Moeda.moeda(Moeda.diminuir(p, t))}"
      f"\nDobro: {Moeda.moeda(Moeda.dobro(p))}"
      f"\nMetade: {Moeda.moeda(Moeda.metade(p))}")


