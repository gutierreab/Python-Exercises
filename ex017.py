# Programa que realiza um sorteio, entre quatro pessoas, utilizando 'import random'.

import random

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

alunos = [a1, a2, a3, a4]
escolhido = random.choice(alunos)
print('O aluno escolhido é:', escolhido)

# Raciocínio lógico utilizado, até a versão final do programa.
# print('O aluno escolhido é:', random.sample(alunos, 1))

# Criado por Amanda Borges Gutierre, em 17 de Agosto de 2022.
