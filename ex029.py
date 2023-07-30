# Programa para contabilizar e localizar a posição de uma letra específica.
# No exemplo abaixo, foi utilizada a letra "A".

frase = str(input('Digite uma frase: ')).upper().strip()

print(f'Quantidade de letra A?', frase.count('A'))
print(f'Em qual posição encontra-se a primeira letra A?', frase.find('A'))

# Lógica utilizada, antes da formatação final:
# print(f'Em qual posição encontra-se a primeira letra A?', frase.find('A')+1) para igualar a posição com a
# do alfabeto

print('Em qual posição encontra-se a última letra A?', frase.rfind('A'))

# Criado por Amanda Borges Gutierre, em 05 de Setembro de 2022.
