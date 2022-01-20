'''crie um programa que leia o nome completo de uma pesoa e mostre:'''
'''- o nome com todas as letras maiúsculas '''
'''- o nome com todas  minusculas '''
'''- quantas letras ao todo (sem considerar espaços) '''
'''- quantas letras tem o primeiro nome '''

'''
a = input(str('digite seu nome completo: ')).strip()

print('seu nome em maiusculo é {}'.format(a.upper()))
print('seu nome em minusculas é {}'.format(a.lower()))
print('seu nome tem ao todo {} letras'.format(len(a) - a.count(' ')))
print('seu primeiro nome tem {} letras'.format(len(a.split()[0])))
'''

nome = str(input('Digite seu Nome Completo: ')).strip()

print('Seu nome com todas as Letra Maiusculas: {} '.format(nome.upper()))

print('Seu nome com todas as Letra Minusculas: {}'.format(nome.lower()))

print('Seu nome tem {} letras ao todo, sem considerar espaços'.format(len(nome) - nome.count(' ')))

print('O seu Primeiro Nome tem {} Letras'.format(len(nome.split()[0])))



