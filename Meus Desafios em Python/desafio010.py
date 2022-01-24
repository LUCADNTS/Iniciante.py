'''crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
 considere U$ 1,00 = R$ 5.47 '''

carteira = float(input('Quanto dinheiro eu tenho: '))

dolar = carteira / 5.47

print('Eu posso comprar {:.2f} U$ dolares com {:.2f} R$ reais'.format(dolar, carteira))