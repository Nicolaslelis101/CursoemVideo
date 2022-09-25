from math import hypot
catop = float(input("Digite o cateto oposto do trinagulo retangulo: "))
catadj = float(input("Digite o cateto adjacente do trinagulo retangulo: "))
h1 = hypot(catop, catadj)
print(f"A hipotanusa deu: {h1:.2f}")

print("-------OU--------")

cat_op = float(input("Digite o cateto oposto do trinagulo retangulo: "))
cat_adj = float(input("Digite o cateto adjacente do trinagulo retangulo: "))
hipo = (cat_op ** 2 + cat_adj ** 2) ** (1/2)
print(f"A hipotanusa deu: {hipo:.2f}")
