# Faca um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

sal_atual = float(input('Me fale o sálario do seu funcionário: '))

sal_novo = float(sal_atual+(sal_atual*0.15))

print('O novo sálario do seu funcionário com 15% de aumento será R${:.2f}'.format(sal_novo))