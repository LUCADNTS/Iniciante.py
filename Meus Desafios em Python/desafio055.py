'''Faça um programa que leia o peso de cinco pessoas. no final,
mostre qual foi o maior e o menor peso lidos '''

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª Pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}Kg'.format(maior))
print('O maior peso é {}Kg'.format(menor))
