''' desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre
 seu status, de acordo com a tabela abaixo:
 - abaixo de 18.5: ABAIXO DO PESO
 - entre 18.5 e 25: PESO IDEAL
 - 25 até 30: SOBREPESO
 - 30 ate 40: OBESIDADE
 - acima de 40:  OBESIDADE MORBIDA
 '''

peso = float(input('Digite seu PESO: '))
altura = float(input('Digite sua ALTURA: '))
imc = peso / (altura**2)

if imc < 18.5:
    print('\033[1;31m SEU IMC É {:.2f} E VOCE ESTA ABAIXO DO PESO !'.format(imc))
    print('\033[1;31m SE ALIMENTE BEM TODOS OS DIAS !')

elif imc <= 25:
    print('\033[1;32m SEU IMC É {:.2f} E VOCE ESTA NO PESO IDEAL !'.format(imc))
    print('\033[1;32m PROCURE MANTER SEMPRE A BOA FORMA !')

elif imc <= 30:
    print('\033[1;33m SEU IMC É {:.2f} E VOCE ESTA COM SOBREPESO !'.format(imc))
    print('\033[1;33M PROCURE SE ALIMENTAR MELHOR !')

elif imc <= 40:
    print('\033[1;33m O SEU IMC É {:.2f} E VOCE ESTA COM OBESIDADE !'.format(imc))
    print('\033[1;33m PROCURE UM MEDICO !!!')

else:
    print('\033[1;31;40m O SEU IMC É {:.2f} E VOCE ESTA COM OBESIDADE MORBIDA !!\033[m'.format(imc))
    print('\033[1;31;40m PROCURE UM MEDICO !!!\033[m')
