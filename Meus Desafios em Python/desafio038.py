''' 
Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais.
'''

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('O numero maior entre {} e {} é : {}'.format(n1, n2, n1))

elif n2 > n1:
    print('O numero maior entre {} e {} é : {}'.format(n1, n2, n2))

else:
    print('''Não existe valor maior entre {} e {}
Os dois valores são iguais! '''.format(n1, n2))
