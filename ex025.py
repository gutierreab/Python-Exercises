# Como fazer um vírus(imagem) usando Turtle.

from turtle import *

# Velocidade dos traços:
speed(100)

# Cor dos traços:
color('cyan')

# Cor do fundo:
bgcolor('black')

b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1

# Criado por Amanda Borges Gutierre, em 05 de Setembro de 2022.
