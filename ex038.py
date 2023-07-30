# Programa para calcular o aumento de um salário.
# Valores fantasia.

salario = float(input('Qual é o valor do seu sálario? R$'))
calculo1 = (salario + salario * 10 / 100) - salario
calculo2 = (salario + salario * 15 / 100) - salario

if salario >= 1250.00:
    print(f'O seu aumento será de R${calculo1:.2f}.')
else:
    print(f'O seu aumento será de R${calculo2:.2f}.')

# Criado por Amanda Borges Gutierre, em 06 de Setembro de 2022.
