''' escreva um programa que converta uma temperatura digitada em ºC e converte para °F '''


'''
temperatura = float(input('Digite uma temperatura: '))
celcios = (temperatura * 1.8) + 32.00
print('A temperatura {}°C é igual a {}°F'.format(temperatura, celcios))
'''

#OU

temperatura = float(input('Digite uma temperatura: '))
celcios = ((temperatura*9)/5) + 32.00
print('A temperatura em Fahrenheit é {}'.format(celcios))
