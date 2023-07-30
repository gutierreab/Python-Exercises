# Programa que verifica em qual ano o alistamento militar deve ser realizado.

from datetime import date

ano = int(input('Digite o ano de seu nascimento: '))
idade = date.today().year - ano
n1 = 18 - idade
n2 = idade - 18

if idade < 18:
    print(f'Ainda falta(m) {n1} ano(s) para você se alistar.')
elif idade == 18:
    print('Está na hora de se alistar.')
else:
    print(f'O seu prazo para se alistar já passou há {n2} ano(s).')

# Criado por Amanda Borges Gutierre, em 21 de Setembro de 2022.
