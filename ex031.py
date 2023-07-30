# Programa para calcular a média escolar de um aluno.


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2

print(f'A sua média foi de: {media}')
if media >= 6.0:
    print('\033[33mParabéns.\033[m')
else:
    print('\033[1;35;40mEstude mais.\033[m')
print('\033[31mFim do semestre.\033[m')

# Criado por Amanda Borges Gutierre, em 06 de Setembro de 2022.
