'''Escreva um programa para aprovar o imprestimo bancario para a compra de uma casa.
o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
calcule o valor da prestaçao mensal, sabendo que ela não pode excerder 30% do salario ou então o
emprestimo sera negado '''

casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite seu Salario: R$ '))
anos = int(input('Digite em quantos anos deseja pagar a casa: '))

meses = anos * 12
prestaçao = casa / meses
salario2 = (salario * 30) / 100


if prestaçao <= salario2:
    print('EM {} ANOS QUE DA {} MESES'.format(anos, meses))
    print('O VALOR DAS PRESTAÇÕES SERA DE {:.2f}R$ POR MÊS'.format(prestaçao))
    print('O VALOR DO IMPRESTIMO ESTA LIBERADO !')

else:
    print('O SEU IMPRESTIMO FOI NEGADO !')
    print('O VALOR DE CADA PARCELA É DE {:.2f}R$'.format(prestaçao))
    print('O VALOR DAS PARCELAS É MAIOR DO QUE 30% ({:.2F}R$) DO SEU SALARIO.'.format(salario2))




