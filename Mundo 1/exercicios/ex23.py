num = int(input("Digite um número entre 0 a 9999: "))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")

print("-----OU------")

n = str(num)
print(f"Unidade: {n[3]}")
print(f"Dezena: {n[2]}")
print(f"Centena: {n[1]}")
print(f"Milhar: {n[0]}")
