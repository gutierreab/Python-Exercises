# Programa para classificar os números decimais.

num = int(input('Digite um número de 0 a 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade: {u}')
print(f'Decimal: {d}')
print(f'Centesimal: {c}')
print(f'Milhar: {m}')

# Criado por Amanda Borges Gutierre, em 05 de Setembro de 2022.
