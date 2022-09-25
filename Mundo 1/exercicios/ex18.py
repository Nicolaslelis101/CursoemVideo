from math import cos, sin, tan, radians
angulo = float(input("Digite o angulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f"O angulo de {angulo} tem o seno {seno:.2f}, cosseno {cosseno:.2f} e tangente {tangente:.2f}")
