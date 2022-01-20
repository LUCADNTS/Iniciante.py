''' faça um programa quue leia o comprimento do cateto oposto
e do cateto adjacente de um triangulo retangulo,
calcule e mostre o comprimento da hipotenusa'''

#  uma maneira dee fazer esse desafio
import math

''' co = float(input('Comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = ((co ** 2) + (ca ** 2)) ** 0.5
print('a hiputenusa vai medir {:.2f}'.format(hi)) '''

# outra maneira de fazer

'''import math
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
tr = math.hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(hi))'''

# outra maneira tambem de chamar é

'''from math import hypot
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = hypot(co, ca)
print('A Hipotenusa é {:.2f}'.format(hi))

# 3 maneiras de fazer o execicio !
'''
co = float(input('digite o cateto oposto: '))
ca = float(input('digite o cateto adjacente: '))
tr = math.hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(tr))





