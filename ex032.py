# Programa para adivinhação de números, utilizando 'Random', para o sorteio dos números de 0 a 5.

import random

descubra = int(input('Digite um número de 0 a 5: '))
n = random.randint(0, 5)
if descubra != n:
    print(f'Você errou. O número era {n}.')
else:
    print(f'Você acertou.')
print('Fim de jogo.')

# Criado por Amanda Borges Gutierre, em 06 de Setembro de 2022.
