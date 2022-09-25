def Leiaint(msg):
    while True:
        try:
           n = int(input(msg))
        except (ValueError, TypeError):
            print("Valor ivalido...")
            continue
        except KeyboardInterrupt:
            print("O usuario não digitou nada.")
            return 0
        else:
            return n


def Leiafloat(msg):
    while True:
        try:
           n = float(input(msg))
        except (ValueError, TypeError):
            print("Valor ivalido...")
            continue
        except KeyboardInterrupt:
            print("O usuario não digitou nada.")
            return 0
        else:
            return n


num1 = Leiaint("Digite um valor: ")
num2 = Leiafloat("Digite um valor: ")
print(f"O número digitado foi: {num1} e {num2}")
