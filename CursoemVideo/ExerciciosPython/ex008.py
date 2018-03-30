# Escreva um programa que leia um valor em metros e o exiba convertido
# em centímetros e milímetros.

metro = float(input('Qual o valor em metros? '))

centim = float(metro*100)
milimet = float(metro*1000)

print('O valor convertido para centímetro é {} cm'.format(centim))
print('O valor convertido para milímetro é {} mm'.format(milimet))