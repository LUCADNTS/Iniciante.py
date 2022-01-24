''' escreva um progrma que leia um numero inteiro qualquer e peça para o
usuario escolher qual sera a base de coversão:
- 1 para binario
- 2 para octal
- 3 para hexadecimal
'''
import math

numero = int(input('Digite um numero: '))

print('''Escolha entre as bases de conversão
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL''')

escolha = int(input('Digite a base de conversão: '))

binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

if escolha == 1:
    print('O Numero {} em Conversão Binaria fica : {}'.format(numero, binario[2:]))
elif escolha == 2:
    print('O Numero {} em Conversão Octal fica : {}'.format(numero, octal[2:]))
elif escolha == 3:
    print('O Numero {} em Conversão Hexadecimal fica : {}'.format(numero, hexadecimal[2:]))
else:
    print('Opção Invalida, Tente Novamente. ')


