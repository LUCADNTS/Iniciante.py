'''faça um programa que leia um numero inteiro qualuqer e  mostre a tabuada na tela'''
numero = int(input('digite um numero: '))
a1 = numero * 1
a2 = numero * 2
a3 = numero * 3
a4 = numero * 4
a5 = numero * 5
a6 = numero * 6
a7 = numero * 7
a8 = numero * 8
a9 = numero * 9
a10 = numero * 10

print('-=' * 20)

print('{} x {} = {}'.format(numero, 1, a1))
print('{} x {} = {}'.format(numero, 2, a2))
print('{} x {} = {}'.format(numero, 3, a3))
print('{} x {} = {}'.format(numero, 4, a4))
print('{} x {} = {}'.format(numero, 5, a5))
print('{} x {} = {}'.format(numero, 6, a6))
print('{} x {} = {}'.format(numero, 7, a7))
print('{} x {} = {}'.format(numero, 8, a8))
print('{} x {} = {}'.format(numero, 9, a9))
print('{} x {} = {}'.format(numero, 10, a10))

print('-=' * 20)

print('ESSA É A TABUADA DO {}'.format(numero))
