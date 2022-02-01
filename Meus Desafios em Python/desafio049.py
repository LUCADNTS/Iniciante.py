'''Refaça o DESAFIO 009, mostrando a tabuada de um numero que o usuario escolher,
só que agora utilizando um laço for'''

numero = int(input('Digite o Numero que Quer a Tabuada: '))

for t in range(1, 11):
   c = numero * t
   print('{} x {} = {}'.format(t, numero, c))

print('TABUADA DO {}'.format(numero))
