''' faça um programa que leia a largura e a altura de uma parede e calcule sua area e a
quantidade de tinta necessaria para pinta-la, sabendo que
cada litro de tinta eu pinto 2m²'''

largura = float(input('largura da parede: '))
altura = float(input('Altura da parede: '))

area = (largura * altura) / 2

print('Eu vou usar {:.2f} latas de tinta para pintar essa parede'.format(area))

