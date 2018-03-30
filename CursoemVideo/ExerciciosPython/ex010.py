# Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos Dólare ela pode comprar.
# Considere US$1,00 = R$3,27

real = float(input('Quanto você tem na carteira R$? '))

dolar = float(real/3.27)

print('Você tem em dólar: ${}'.format(dolar))