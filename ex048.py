# Programa para calcular se uma promoção será habilitada, diante de uma forma de pagamento específica.

preço = float(input('Digite o preço do produto: R$'))
condição = int(input('Selecione a forma de pagamento. Digite: \n'
                     '1 = Dinheiro/cheque (10% de desconto);\n'
                     '2 = Cartão (5% de desconto;\n'
                     '3 = Cartão 2x;\n'
                     '4 = Cartão 3x (20% de juros).\n'))
if condição == 1:
    dinheiro_cheque = (preço - preço * 10 / 100)
    print(f'O preço a pagar será de R${dinheiro_cheque:.2f}.')
elif condição == 2:
    cartão = (preço - preço * 5 / 100)
    print(f'O preço a pagar será de R${cartão:.2f}.')
elif condição == 3:
    cartão2x = (preço / 2)
    print(f'O preço a pagar será de 2x de R${cartão2x:.2f}.')
elif condição == 4:
    cartão3x = (preço + preço * 20 / 100) / 3
    print(f'O preço a pagar será de 3x de R${cartão3x:.2f}.')
else:
    print('Selecione uma opção de pagamento.')

# Criado por Amanda Borges Gutierre, em 4 de Outubro de 2022.
