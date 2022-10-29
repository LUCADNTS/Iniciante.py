''' 
crie um programa que leia dois números e mostre a soma entre eles
n = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))

s = (n + n2)

print('a soma entre {} e {} é : {}'.format(n, n2, s))
'''

from asyncore import loop


a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

s = a + b
print('A soma entre {} e {} é: {}'.format(a, b , s))

