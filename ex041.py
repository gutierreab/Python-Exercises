# Programa para verificar se um empréstimo será realizado, ou não.
# Valores fantasia.

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
tempo = float(input('Em quantos meses pretende efetuar o pagamento? '))

if casa/tempo > (salario + salario * 30/100) - salario:
    print('O seu empréstimo não será solicitado. O valor mensal da parcela é excedente a 30% do seu salário.')
else:
    print('O seu empréstimo será solicitado com sucesso.')

# Criado por Amanda Borges Gutierre, em 20 de Setembro de 2022.
