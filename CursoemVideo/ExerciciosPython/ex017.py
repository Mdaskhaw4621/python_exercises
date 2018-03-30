# Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente
# triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

'''from math import pow, sqrt

b = float(input('Qual o comprimento do cateto oposto: '))
c = float(input('Qual o comprimento do cateto adjacente: '))

a = sqrt((pow(b, 2)+pow(c, 2)))

print('O comprimento da hipotenusa é de: {:.2f} cm'.format(a))'''

from math import hypot

b = float(input('Qual o comprimento do cateto oposto: '))
c = float(input('Qual o comprimento do cateto adjacente: '))

a = hypot(b, c)

print('O comprimento da hipotenusa é de: {:.2f} cm'.format(a))
