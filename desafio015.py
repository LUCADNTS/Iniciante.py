''' escreva um programa que pergunte a quantidade de KM
percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$ 0.15 por KM rodado
'''

km = float(input('Quantos Km foram percorridos com o carro: '))
dias = float(input('Quantos dias foi alugado: '))
precokm = (0.15 * km)
precocar = (dias * 60.00)
total = precokm + precocar
print('O preço do alugueu do carro por DIA alugado é {:.2f}R$'.format(precocar))
print('O preço dos KM rodados é {:.2f}R$'.format(precokm))
print('O total a pagar ficou {:.2f}R$'.format(total))
