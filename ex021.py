# Programa que realiza substituição de um termo na frase, além de outras funções, tais, como:
# contabilizar a quantidade de uma determinada letra, ou, ainda, a quantidade de letras na oração.

frase = 'Aprendendo Python'
print(frase.replace('Python', 'Java'))

print(frase.count('o'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.find('ndo'))
print(frase[:5])
print(frase[9::3])
print(frase[3:7])
print(frase.title())
print(frase.split())
print('-'.join(frase.split()))
print(len(frase))

# Criado por Amanda Borges Gutierre, em 23 de Agosto de 2022.
