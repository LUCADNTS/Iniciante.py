'''faça um algoritmo que leia o salario de um funcionario e mostre na tela o seu novo salario com 15% de aumento'''

salario = float(input('Digite seu salario: '))
calculo = (salario * 15) / 100
aumento = salario + calculo
print('O seu novo salario é {:.2f} com 15% de aumento'.format(aumento))
