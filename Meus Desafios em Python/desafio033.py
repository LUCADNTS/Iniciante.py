''' Faça um programa que leia 3 numero e mostre qual é o maior e qual o menor'''


'''
n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))
n3 = int(input('Numero 3: '))

if n1 > n2 and n1 > n3:
    print('O numero maior é {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O numero maior é {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O numero maior é {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('O numero menor é {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O numero menor é {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('O numero menor é {}'.format(n3))
'''

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))