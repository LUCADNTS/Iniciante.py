''' 
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- a vista dinheiro/cheque: 10% de desconto
- a vista no cartão: 5% e desconto
- em até 2X no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

produto = float(input('Preço do Produto: '))

print('{:=^50}\n'.format(' LOJAS LUCAS '))
print('- Temos as Seguintes Condições de Pagamento\n')
print('[1] A vista, Dinheiro ou Cheque com 10% desconto')
print('[2] A vista no Cartão com 5% Desconto')
print('[3] Em 2x no Cartão')
print('[4] Em 3x ou Mais no Cartão com 20% de Juros\n')
print('{:=^50}\n'.format(' LOJAS LUCAS '))

fpag = int(input('\nEscolha uma forma de pagamento: '))

if fpag == 1:
    a = produto * 10 / 100
    total = produto - a
    print('A forma de pagamento via\033[1;32m Cartão/Cheque voce tem 10% desconto.')
    print('total a pagar R${:.2f}'.format(total))

elif fpag == 2:
    b = produto * 5 / 100
    total = produto - b
    print('A forma de pagamento\033[1;32m a vista no cartão voce tem 5% de desconto.')
    print('Total a pagar R${:.2f}'.format(total))

elif fpag == 3:
    c = produto / 2
    print('A forma de pagamento em\033[1;33m 2x no Cartão não tem desconto.')
    print('Total a pagar 2x de R${:.2f}'.format(c))

elif fpag == 4:
    d = produto * 20 / 100
    total = produto + d
    totalparc = int(input('Quantas parcelas?: '))
    parcela = total / totalparc
    print('A forma de pagamento selecionada tem\033[1;31m juros de 20%.')
    print('Total de parcelas {}x e o preço das parcelas é: R${:.2f}'.format(totalparc, parcela))
    print('Totalizando preço final com juros R${:.2f}'.format(total))
