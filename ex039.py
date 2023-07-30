# Programa para verificar se as medidas informadas formam um triângulo.

a = float(input('Digite o primeiro tamanho: '))
b = float(input('Digite o segundo tamanho: '))
c = float(input('Digite o terceiro tamanho: '))

if (a + b) > c and (c + b) > a and (a + c) > b:
    print('As retas formam um triângulo.')
else:
    print('As retas não formam um triângulo.')

# Criado por Amanda Borges Gutierre, em 06 de Setembro de 2022.
