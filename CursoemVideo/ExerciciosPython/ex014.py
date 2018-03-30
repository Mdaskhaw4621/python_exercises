# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

C = float(input('Qual a temperatura em Celsius agora? '))

F = float(((9*C)/5)+32)

print('A temperatura de {}°C equivale a {}°F.'.format(C, F))