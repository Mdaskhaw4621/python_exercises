# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção inteira.
from math import trunc

number = float(input('Digite um número: '))

trunc = trunc(number)

print('O número digitado foi {}, e sua parte inteira é {}.'.format(number, trunc))