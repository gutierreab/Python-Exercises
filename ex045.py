# Programa que verifica se um aluno foi reprovado no período escolar, ou se precisará fazer recuperação.
# Valores fantasia.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('Você foi reprovado. Sua nota está abaixo da média.')
elif media == 5.0 or media <= 6.9:
    print('Você está de recuperação. Bons estudos')
else:
    print('Você está aprovado. \033[4;36mParabéns!\033[m')

# Criado por Amanda Borges Gutierre, em 21 de Setembro de 2022.
