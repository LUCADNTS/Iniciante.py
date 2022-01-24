'''escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostrar uma mensagem dizendo que
ele foi multado. A multa vai custar R$7,00  por KM acima do limite'''

import math

'''
a = float(input('Velocidade : '))

print('LIMITE DE VELOCIDADE É 80KM !')
print('CASO ESTIVER ACIMA DO LIMITE DE VELOCIDADE SERÁ MULTADO!')
print('O VALOR É DE 7.00R$ POR KM ACIMA DO LIMITE !')

km = float(a - 80)
multa = float(km * 7)

if a < 80:
    print('Você esta dentro do limite de velocidade, Boa Viagem ')
elif a > 80:
    print('Voce foi multado por esta acima do limite de 80KM !\nO valor da sua multa é no valor de: {:.2f} R$'.format(multa))
'''

'''
velocidade = float(input('Coloque a velocidade: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Voce passou do limite de velocidade e por isso levou uma multa de {:.2f}R$'.format(multa))
print('Tenha uma boa viagem')
'''

velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade - 80) * 7.0

if velocidade > 80:
    print('VOCE FOI MULTADO !\nEXCEDEU O LIMITE DE VELOCIDADE !')
    print('A SUA MULTA FOI DE {}'.format(multa))

else:
    print('TENHA UMA BOA VIAGEM, DIRIJA COM SEGURANÇA !')

