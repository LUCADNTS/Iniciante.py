'''CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCE '''

import random
import time

print('VAMOS JOGAR JOKENPÔ !')
print('''Escolha entre:

[0] PEDRA
[1] PAPEL
[2] TESOURA

''')

jogador = int(input('Escolha: '))

print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PÔ')
time.sleep(0.51)

lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.randint(0, 2)

print('=' * 40)
print('JOGADOR: {0}'.format(lista[jogador]))
print('COMPUTADOR: {}'.format(lista[computador]))
print('=' * 40)

if computador == 0:   #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('O JOGADOR VENCEU !')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU !')
    else:
        print('JOGADA INVALIDA !')

elif computador == 1:   #COMPUTADOR JOGOU PAPEL
    if jogador ==0:
        print('O COMPUTADOR VENCEU !')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('O JOGADOR VENCEU !')
    else:
        print('JOGADA INVALIDA !')

elif computador == 2:   #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('O JOGADOR VENCEU !')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU !')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA !')
