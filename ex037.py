# Programa para verificar qual número é o menor e o maior, dentro de uma lista.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

numeros = [n1, n2, n3]

# Lógica utilizada, até formatação final.
# numeros.sort(reverse=True)
# print(f'Os números são: {numeros.}')

print(f'O maior número é {max(numeros)}. E o menor, {min(numeros)}.')

# Criado por Amanda Borges Gutierre, em 06 de Setembro de 2022.
