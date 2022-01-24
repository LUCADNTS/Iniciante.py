''' 
faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- se ele ainda vai se alistar ao serviço militar
- se é a hora de se alistar
- se ja passou do tempo do alistamento.
Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.
'''

import datetime
import time

nasc = int(input('Digite o seu ano de nascimento: '))
anoatual = datetime.date.today().year
idade = anoatual - nasc

if idade == 18:
    print('Se apresente ao Serviço Militar IMEDIATAMENTE !')

elif idade > 18:
    saldo = idade - 18
    ano = anoatual - saldo
    print('Voce nasceu em {}'.format(nasc))
    print('Voce tem {} e deveria ter se alistado a {} atras'.format(idade, saldo))
    print('No ano de {}'.format(ano))

elif idade < 18:
    saldo = 18 - idade
    ano = anoatual + saldo
    print('Voce nasceu em {}'.format(nasc))
    print('Voce tem {} ano(s) e ainda faltam {} ano(s) para se alistar'.format(idade, saldo))
    print('No ano de {}'.format(ano))





