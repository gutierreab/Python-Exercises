# Programa que verifica se os números digitados são iguais, ou, qual o maior e o menor.

n1 = int(input('Digite um número qualquer: '))
n2 = int(input('Digite outro número: '))
n3 = [n1, n2]
if n1 == n2:
    print('Os dois números digitados são iguais.')
else:
    print(f'O número maior é {max(n3)} e o menor {min(n3)}.')

# Criado por Amanda Borges Gutierre, em 21 de Setembro de 2022.
