''' faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados '''

'''
num = int(input('digite um numero de 0 a 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
'''

numero = int(input('Digite um Numero de [0 a 9999] : '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('O numero tem: {} unidades'.format(unidade))
print('O nuimero tem: {} dezenas'.format(dezena))
print('O numero tem: {} centenas'.format(centena))
print('O numero tem: {} milhar'.format(milhar))
