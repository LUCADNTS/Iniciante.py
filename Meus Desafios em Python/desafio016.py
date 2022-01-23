'''crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porçao inteira'''
''' Ex: digite um numero 6.124   /   O numero 6.124 tem a parte inteira '''

# posso usar -> ( import math )

import math
'''a = float(input('Digite um numero: '))
print('A parte inteiro do numero {} é {}'.format(a, math.trunc(a)))'''

# ou posso usar tambem -> ( from math import trunc )

'''from math import trunc
a = float(input('digite um numero: '))
print('A parte inteira do numero {} é {}'.format(a, trunc(a)))'''

# ou podemos fazer dessa maneira

'''num = float(input('digite um valor: '))
print('o valor digitado é {} e a parte inteira é {}'.format(num, int(num)))'''


numero = float(input('digite um numero real: '))
print('A parte interia desse numero real é {}'.format(math.trunc(numero)))
