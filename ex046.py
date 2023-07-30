# Programa que simula uma competição esportiva, de natação, e verifica em qual categoria o competidor deve
# participar.

from datetime import date

print('-=' * 10, '\033[0;36mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m', '-=' * 10)

ano = int(input('Para saber em qual categoria você participará, digite o ano de seu nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('\nVocê participará da categoria MIRIM.')
elif idade == 10 or idade <= 14:
    print('\nVocê participará da categoria INFANTIL.')
elif idade == 15 or idade <= 19:
    print('\nVocê participará da categoria JÚNIOR.')
elif idade == 20:
    print('\nVocê participará da categoria SÊNIOR.')
else:
    print('\nVocê participará da categoria MASTER.')

# Criado por Amanda Borges Gutierre, em 21 de Setembro de 2022.
