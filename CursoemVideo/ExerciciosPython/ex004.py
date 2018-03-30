# Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
# todas as informações possiveis sobre ele.

x = input('Digite alguma coisa: ')

print(type(x))
print('É alfanúmerico? ', x.isalnum())
print('É constituido por letras somente? ', x.isalpha())
print('Está tudo minúsculo? ', x.islower())
print('É constituido apenas por números? ', x.isnumeric())
print('Está tudo maiúsculo? ', x.isupper())
