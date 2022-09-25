import Moeda

p = float(input("Digite o preço: "))
t = float(input("Digite a taxa: "))
print(f"Aumento: {Moeda.aumentar(p, t)}"
      f"\nRedução: {Moeda.diminuir(p, t)}"
      f"\nDobro: {Moeda.dobro(p)}"
      f"\nMetade: {Moeda.metade(p)}")


