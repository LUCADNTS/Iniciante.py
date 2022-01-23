'''escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 e 5 e peça para o
usuario tentar descobrir qual foi o numero escolhido pelo computador
O programa devera escrever na tela se o usuario venceu ou perdeu '''
'''
import random

x = int(input('digite um numero e veja se voce acertou: '))
lista = random.randint(0, 5)
if x == lista:
    print('PARABENS !! VOCE VENCEU')
else:
    print('VOCE PERDEU, TENTE NOVAMENTE')
print('O NUMERO É: {}'.format(lista))
'''

'''
import random
from time import sleep
computador = random.randint(0, 5)
jogador = int(input('Digite um numero de 0 a 5 : '))
print('Processando. . . ')
sleep(2)
if computador == jogador:
    print('Parabens voce acertou')
else:
    print('Voce errou, o numero que eu pensei foi {}'.format(computador))
'''
import random

computador = random.randint(0, 5)
numero = int(input('Digite um numero de 0 a 5 e tente ganhar do computador: '))\


if numero == computador:
    print('Parabens !!!!\nVoce venceu o computador e acertou o numero que ele estava pensando !')
else:
    print('Tente novamente !\nO Computador te venceu !\nO numero que ele pensou foi {} '.format(computador))

