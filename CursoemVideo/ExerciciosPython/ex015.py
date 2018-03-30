# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade  de dias pelos quais foi alugado. Calcule o preco a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por Km rodado.

dia_alug = int(input('Quantos dias o carro esteve alugado? '))
km_rodado = int(input('Quantos Km rodados? '))

preco_dia = dia_alug * 60
preco_km = km_rodado * 0.15
total = preco_dia + preco_km

print('O total a ser pago é de R${}'.format(total))
