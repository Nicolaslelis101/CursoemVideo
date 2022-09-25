peso = float(input("Qual seu peso: "))
altura = float(input("Qual sua altura: "))
imc = peso / (altura ** 2)
print(f"O IMC da pessoa é: {imc:.2f}")
if imc < 18.5:
    print("Abaixo do peso normal.")
elif 18.5 <= imc < 25:
    print("Peso normal.")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 40:
    print("Obesidade.")
elif imc >= 40:
    print("Obesidade morbida")
