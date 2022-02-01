'''crie um programa que mostre na tela todos os numeros pares que estão
no intervalo de 1 e 50 '''


'''
for num in range(1, 51):
    if num % 2 == 0:
        print('{} '.format(num), end="")
print('\nEssses são os números pares de 1 a 50')
'''



for n in range(2, 51, 2):
    print('{} '.format(n), end='')
