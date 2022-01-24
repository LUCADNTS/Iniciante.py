'''
faça um programa que leia o angulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse angulo
'''

# uma maneria de fazer é :

'''
import math
angulo = float(input('Digite um numero: '))
seno = math.sin(math.radians(angulo))

print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))

print('O angulo é {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))

print('O angulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))
'''

# posso simplificar usando:

'''
from math import radians, sin, cos, tan

angulo = float(input('Digite um numero: '))
seno = sin(radians(angulo))
print('o angulo de {} tem o seno de: {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('o angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('0 angulo de {} tem o tangente de {:.2f}'.format(angulo, tangente))
'''

import math

angulo = float(input('DIGITE O ANGULO: '))

seno = math.sin(math.radians(angulo))
print('o seno de {:.2f} é'.format(seno))

cosseno = math.cos(math.radians(angulo))
print('o cosseno é {:.2f}'.format(cosseno))

tangente = math.tan(math.radians(angulo))
print('o tangente é {:.2f}'.format(tangente))

print('esses são o seno, cosseno e tangente do angulo {}'.format(angulo))






