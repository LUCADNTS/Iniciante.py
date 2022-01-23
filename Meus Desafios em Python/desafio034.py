'''Escreva um programa que pergunte um salario de um funcionario e calcule o valor do seu aumento.
para salarios superiores a R$1.250,00 calcule um aumento de 10%
para inferiores ou iguais, o aumento é de 15%'''
import math

'''
salario = float(input('Qual o seu salario: '))

a = salario * 10 / 100
aumento = salario + a

b = salario * 15 / 100
aumento2 = salario + b

if salario > 1250:
    print(' O aumento foi {}R$ e seu salario agora passa a ser {}R$'.format(a, aumento))

if salario <= 1250:

    print('o aumento foi {}R$ e seu salario agora passa a ser {}R$'.format(b, aumento2))
'''




salario = float(input('Digite o salario do Funcionario: '))

if salario > 1250:
    aumento = (salario * 10) / 100
    total = salario + aumento
    print('O salario com aumento de 10% ficou : {:.2f}R$'.format(total))

if salario <= 1250:
    aumento2 = (salario * 15) / 100
    total2 = salario + aumento2
    print('O salario com aumento de 15% ficou : {:.2f}R$'.format(total2))
