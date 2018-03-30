# Crie um algoritmo que leia um número e mostre o seu dobro,
# triplo e raiz quadrada.

number = float(input('Digite um numero: '))

dobro = float(number * 2)
triplo = float(number * 3)
raiz = float(number ** (1/2))

print('O triplo de {} é {}'.format(number, triplo))
print('O dobro de {} é {}'.format(number, dobro))
print('A raiz quadrada de {} é {}'.format(number, raiz))