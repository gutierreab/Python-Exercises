# Programa que calcula as razões trigonométricas (Seno, Cosseno e Tangente).

import math

angulo = float(input('Digite um número: '))

ang = math.radians(angulo)
seno = math.sin(ang)
coseno = math.cos(ang)
tan = math.tan(ang)

print(f'No ângulo de {ang:.2}, o seno é {seno:.2}, o coseno é {coseno:.2} e a tangente é {tan:.2}')

# Criado por Amanda Borges Gutierre, em 10 de Agosto de 2022.


