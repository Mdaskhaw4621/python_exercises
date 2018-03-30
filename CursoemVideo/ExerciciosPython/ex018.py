# Faca um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = int(input('Digite o ângulo: '))

sen = math.sin(ang)

print('O seno de {}° é {:.2f}.'.format(ang, sen))

