'''Crie um programa que leia um ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores '''

from datetime import date

data = date.today().year
totmaior = 0
totmenor = 0

for i in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu: '.format(i)))
    idade = data - nasc
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1

print('Tivermos {} pessoas maiores de idade '.format(totmaior))
print('Tivemos {} pessoas menores de idade '.format(totmenor))
