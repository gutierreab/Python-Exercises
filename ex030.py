# Programa que informa qual a primeira e a última palavras utilizadas na oração.
# No exemplo abaixo, foi utilizada a variável de um nome completo.

nome = str(input('Digite o seu nome completo: '))
n1 = nome.split()

print(f'Seu primeiro nome é {n1[0]}')
print(f'Seu último nome é {n1[-1]}')

# Lógica apresentada, antes da formatação final:
# print(f'Qual é o primeiro nome?', {nome.split()})

# Criado por Amanda Borges Gutierre, em 05 de Setembro de 2022.
