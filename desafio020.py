'''o mesmo professor do desafio anterior quer sortear
a ordem de apresentaçao de trabalhos dos alunos, faça um programa
que leia o nome dos quatro alunos e mostre a ordem sorteda'''

import random
'''
a = input('Aluno 1: ')
b = input('Aluno 2: ')
c = input('Aluno 3: ')
d = input('Aluno 4: ')
lista = [a, b, c, d]
random.shuffle(lista)
print('A ordem para apresentação do trabalho É')
print(lista)
'''


'''
from random import shuffle

a1 = input('aluno 1: ')
a2 = input('aluno 2: ')
a3 = input('aluno 3: ')
a4 = input('aluno 4: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('a seguinte lista apresentara os trabalhos')
print(lista)
'''
import random

# primeiro peço os nomes dos aluno

aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))

#depois faço uma lista com esses nomes

lista = [aluno1, aluno2, aluno3, aluno4]

#depois uso a funcionalidade shuffle de dentro do modulo random para misturar os nomes

escolhido = random.shuffle(lista)

# depois só preciso passar a lista ja atualizada e misturada

print('A ordem de apresentação vai ser: {} '.format(lista))
