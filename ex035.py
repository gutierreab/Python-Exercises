# Programa para calcular custos de pedágio de uma viagem, com parâmetro de 200km de distância, ou acima.
# Valores fantasia.

distancia = float(input('Qual a distância(Km) da viagem? '))
calculo1 = distancia*0.50
calculo2 = distancia*0.45

if distancia <= 200.00:
    print(f'A sua viagem terá custo de R${calculo1:.2f}.')
else:
    print(f'A sua viagem terá custo de R${calculo2:.2f}.')
print('\033[7;40;35mBoa viagem.\033[m')

# Criado por Amanda Borges Gutierre, em 06 de Setembro de 2022.
