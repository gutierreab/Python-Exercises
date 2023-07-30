# Programa para calcular se o ano é bissexto, ou não.

import calendar
ano = int(input('Digite o ano desejado: '))
bissexto = calendar.isleap(ano)

if bissexto == True:
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')
    
# Criado por Amanda Borges Gutierre, em 06 de Setembro de 2022.
