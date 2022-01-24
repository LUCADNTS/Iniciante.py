''' desenvolva um programa que pergunte a distancia de uma viagem em KM.
calcule o preço da passagem, cobrando R$0,50 por KM para viagens
de até 200KM e R$0,45 para viagens mais longas'''

import math

'''
km = float(input('Qual a distancia da viagem em KM : '))

if km < 200:
    a = float(km * 0.50)
    print('A passagem custara {:.2f}R$'.format(a))
elif km > 200:
    b = float(km * 0.45)
    print('A passagem custara {:.2f}R$'.format(b))
print('BOA VIAGEM !')
'''

'''
distancia = float(input('digite a distancia da viagem: '))

if distancia <= 200:
    preço = distancia * 0.50
    print('o valor da viagem vai ser: {:.2f}R$ '.format(preço))
else:
    preço = distancia * 0.45
    print('o valor da viagem vai ser {:.2f}R$ '.format(preço))
print('tenha uma boa viagem')
'''

'''
distancia = float(input('digite a distancia: '))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('o preço sera {:.2f}R$'.format(preço))
print('Boa Viagem !')
'''


distancia = float(input('Digite a distancia em KM: '))

passagem1 = distancia * 0.50
passagem2 = distancia * 0.45

if distancia <= 200:
    print('O preço da passagem é {:.2f}R$'.format(passagem1))
else:
    print('O preço da passagem é {:.2f}R$'.format(passagem2))

print('Boa Viagem !')




