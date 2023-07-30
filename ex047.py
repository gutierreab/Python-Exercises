# Programa para calcular o Índice de Massa Corporal (IMC).

peso = float(input('Digite o seu peso(kg): '))
altura = float(input('Digite a sua altura(m): '))
IMC = peso / (altura ** 2)

print(f'O seu IMC é de {IMC:.2f}.')
if IMC < 18.5:
    print('Você está abaixo do peso.')
elif IMC == 18.5 or IMC <= 24.9:
    print('Você está com o seu peso ideal.')
elif IMC == 25.0 or IMC <= 29.9:
    print('Você está com sobrepeso.')
elif IMC == 30.0 or IMC <= 39.9:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')

# Criado por Amanda Borges Gutierre, em 21 de Setembro de 2022.
