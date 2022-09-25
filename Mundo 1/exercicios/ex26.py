frase = input("Digite uma frase: ").upper().strip()
print(f"A frase tem {frase.count('A')} de 'A'. Primeira aparição {frase.find('A')+1} e a última {frase.rfind('A')+1}")
