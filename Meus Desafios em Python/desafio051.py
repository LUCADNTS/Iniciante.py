'''desenvolva um programa que leia o primeiro termo e a razão de um PA.
no final, mostre os 10 primeiros termos dessa progressão'''

termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo1 + (10 - 1) * razao

for i in range(termo1, decimo + razao, razao):
    print('{}'.format(i), end=' -> ')
print('\nFIM DA P.A')