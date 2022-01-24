''' Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto '''
produto = float(input('Digite o preço do produto: '))

desconto = (produto * 5) / 100
preço = produto - desconto

print("O produto com desconto de 5% esta custando {:.2f}R$".format(preço))