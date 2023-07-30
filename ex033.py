# Programa para cálculo de valores de multas.
# Valores fantasia.

velocidade = float(input('A velocidade do seu carro era de: '))
calculo = (velocidade-80)*7.00

if velocidade > 80:
    print(f'Você receberá uma multa de \033[1;35;40mR${calculo:.2f}\033[m, devido à velocidade acima do limite '
          f'permitido, de 80Km/h.')
else:
    print('Você está livre de multas.')

# Criado por Amanda Borges Gutierre, em 06 de Setembro de 2022.
