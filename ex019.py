# Programa que realiza uma lista de alunos, em ordem aleatória.

from random import shuffle

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Quarto aluno: '))
a4 = str(input('Quinto aluno: '))

alunos = [a1, a2, a3, a4]
shuffle(alunos)

print('A ordem escolhida é:', alunos)

# Raciocínio lógico utilizado, até a versão final do programa.
# print('A ordem escolhida é:', random.sample(alunos, 4))

# Criado por Amanda Borges Gutierre, em 17 de Agosto de 2022.
