vel = float(input("Digite a velocidade do carro: "))
if vel > 80:
    multa = (vel - 80) * 7
    print(f"Foi multado. Multa: {multa:.2f}")
else:
    print("Tudo certo.")
