# Programa que realiza a conversão de um número decimal em: Binário, Octal e Hexadecimal.

n = int(input('Digite um número qualquer: '))
conversao = int(input('Selecione uma opção abaixo:\n'
                      'Digite 1 para conversão em binário;\n'
                      'Digite 2 para conversão em octal;\n'
                      'Digite 3 para conversão em hexadecimal.\n'))
if conversao == 1:
    print(bin(n))
elif conversao == 2:
    print(oct(n))
elif conversao == 3:
    print(hex(n))
else:
    print('Selecione uma opção válida.')

# Criado por Amanda Borges Gutierre, em 20 de Setembro de 2022.
