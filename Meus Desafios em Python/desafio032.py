'''faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO'''

import math
import datetime

'''
ano = int(input('digite um Ano: '))

if ano == 0:
    ano = datetime.date.today().year
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano de {} é um ano bissexto'.format(ano))

else:
    print('o ano de {} não é um ano bissexto'.format(ano))
'''

ano = int(input('digite o ano que queria saber se é bissexto: '))

if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto !'.format(ano))
else:
    print('O ano {} não é bissexto !'.format(ano))




