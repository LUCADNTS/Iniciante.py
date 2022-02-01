'''faça um programa que calcule a soma entre todos os números impares que são
múltiplos de três e que se encontram no intervalo de 1 até 500.'''

cont = 0
soma = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma = soma + num
        cont = cont + 1
print('{} é o total de numeros que são multiplos de 3'.format(cont))
print('A soma dos numeros impares multiplos de 3 em um intervalo de 1 a 500 é {}'.format(soma))


