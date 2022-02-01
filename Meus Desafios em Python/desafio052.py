'''faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.'''

n = int(input('Digite um Numero: '))
tot = 0
print('''\n---> UM NÚMERO \033[33mPRIMO\033[m SÓ PODE SER DIVIDIDO 2 VEZES, POR 1 E POR ELE MESMO.
SENDO ASSIM: ''')
print('='*60)

for i in range(1, n+1):
    if n % i == 0:
        print('\033[31m', end='')
        tot = tot + 1
    else:
        print('\033[32m', end='')
    print('{} '.format(i), end='')

print('\n''\033[mO NúMERO {} É DIVISIVEL {} VEZES'.format(n, tot))

if tot == 2:
    print('\nELE É UM NÚMERO PRIMO')
else:
    print('\nELE NÃO É UM NÚMERO PRIMO')
print('='*60)
