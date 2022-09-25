try:
    n1 = int(input("Numero: "))
    n2 = int(input("Numero: "))
    r = n1 / n2
except (ValueError, TypeError):
    print("OS tipos de dados foram incorretos.")
except ZeroDivisionError:
    print("Não é possivel dividir zero!")
except KeyboardInterrupt:
    print("Você não digitou nada....")
except Exception as erro:
    print(f"Ocorreu um problema foi {erro.__class__}!!!!")
else:
    print(f"Resultado {r}")
finally:
    print("Volte sempre.")
