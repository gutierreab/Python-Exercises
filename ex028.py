# Programa para localizar uma palavra específica em uma oração, texto, ou nome composto.
# No exemplo abaixo, o localizador filtra se há a palavra "Silva" no nome digitado.

nome = str(input('Digite o seu nome completo: ')).strip().upper().split()

print('Seu nome tem Silva?', 'SILVA' in nome)

# Criado por Amanda Borges Gutierre, em 05 de Setembro de 2022.









