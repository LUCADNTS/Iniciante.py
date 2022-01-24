''' 
A Confederação nacional de natação precisa de um programa que leia o ano  de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- ate 19 anos: JUNIOR
- até 25 anos: SÊNIOR
- acima : MASTER
'''

import datetime

ano = int(input('Digite o seu ano de nascimento: '))
ano2 = datetime.date.today().year
idade = ano2 - ano

if idade < 9:
    print('Voce tem {} ano(s)'.format(idade))
    print('Você é um Nadador MIRIM')

elif idade <= 14:
    print('Voce tem {} ano(s)'.format(idade))
    print('Você é um Nadador INFANTIL')

elif idade <= 19:
    print('Voce tem {} ano(s)'.format(idade))
    print('Você é um Nadador JUNIOR')

elif idade <= 25:
    print('Voce tem {} ano(s)'.format(idade))
    print('Você é um Nadador SENIOR')

else:
    print('Voce tem {} ano(s)'.format(idade))
    print('Você é um Nadador MASTER !')
