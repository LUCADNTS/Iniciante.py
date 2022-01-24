''' Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario
se elas podem ou não formar um triangulo '''

import math

'''
r1 = float(input('reta 1: '))
r2 = float(input('reta 2: '))
r3 = float(input('reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('esses seguimento podem formar um triangulo')
else:
    print('essees seguimentos não podem formar um triangulo')
'''

r1 = int(input('reta 1: '))
r2 = int(input('reta 2: '))
r3 = int(input('reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses seguimentos formam um triangulo')
else:
    print('Esses seguimentos não formam um triangulo')

# alguns exercicios eu faço 2 vezes pra melhorar o aprendizado