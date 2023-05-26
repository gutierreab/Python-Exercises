# Programa que lê um termo digitado, e o classifique conforme a estrutura apresentada.
# Isto é, se é de ordem númerica, alfabética, ou ambos.

X = input('Digite algo: ')

print(f'É numérico?', {X.isnumeric()})
print(f'Tem espaços?', {X.isspace()})
print(f'Tem letras maiúsculas?', {X.isupper()})
print(f'Tem letras minúsculas?', {X.islower()})
print(f'É alfanúmerico?', {X.isalnum()})

# Criado por Amanda Borges Gutierre, em 04 de Agosto de 2022.
