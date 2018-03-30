# Faca um algoritmo que leia o preco de um produto e mostre
# seu novo preço, com 5% de desconto.

pre_ant = float(input('Insira o valor do produto: '))

n_preco = float(pre_ant-(pre_ant*0.05))

print('O novo preço com 5% de desconto é R${:.2f}'.format(n_preco))
