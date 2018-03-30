# Faca  um programa que leia a largura e a altura de uma parede em
# metros, calcule a sua área e a quantidade de tinta necessária para
# pintá-los, sabendo que cada litro de tinta, pinta uma área de 2 m².

heigth = float(input('Qual a altura da parade? '))
length = float(input('Qual a largura da parede? '))

A = float(heigth*length)
qtd_tinta = int(A*2)

print('A área da parede é {}m², e a quantidade de tinta necessária para pintá-la é {}L.'.format(A, qtd_tinta))
