# Faca um programa que leia um número inteiro e mostre na tela o seu
# sucessor e seu antecessor

number = int(input('Aperte um número do seu teclado: '))

anteces = int(number - 1)
suces = int(number + 1 )

print('O {} tem como respectivo antecessor o {} e como respectivo sucessor o {}.'.format(number, anteces, suces))