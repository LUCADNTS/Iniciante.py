'''um professor quer sortear um dos seus quatro alunos
para limpar o quadro, faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido'''

'''import random

a = input('digite o noe do primeiro aluno: ')
b = input('digite o nome do segundo aluno: ')
c = input('digite o nome do terceiro aluno: ')
d = input('digite o nome do quarto aluno: ')

lista = [a, b, c, d]

escolhido = random.choice(lista)

print('o aluno escolhido foi o {}'.format(escolhido))'''


# posso usar outra maneira pegando uma funcionalidade de dentro do modulo 'random'
'''
from random import choice

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O Aluno Escolhido para limpar o quadro foi o {}'.format(escolhido))
'''
import random

aluno1 = str(input('Nome aluno 1: '))
aluno2 = str(input('Nome aluno 2: '))
aluno3 = str(input('Nome aluno 3: '))
aluno4 = str(input('Nome aluno 4: '))

lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = random.choice(lista)
print('{} foi o escolhido para limpar a lousa'.format(escolhido))
