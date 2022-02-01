'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
Ex: APOS A SOPA / A SACADA DA CASA / A TORRE DA DERROTA / O LOBO AMA O BOLO '''


frase = str(input('Digite um Frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = juntar[::-1]

'''
inverso = ''
for l in range(len(juntar) - 1, -1, -1):
    inverso = inverso + juntar[l]
'''

print('O inverso de {} é {}'.format(juntar, inverso))

if inverso == juntar:
    print('Temos um Palindromo')
else:
    print('Não é um Palindromo')


#--------------------------------------------------------------

'''
frase = input("Qual a frase? ").upper().replace(" ", "")
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")
'''