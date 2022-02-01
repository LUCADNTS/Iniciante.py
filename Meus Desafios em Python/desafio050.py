''' desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas
daqueles que forem pares, se o valor digitado for impar, desconsidere-o'''

cont = 0
soma = 0
for i in range(1, 7):
    numero = int(input('Digite o {}º valor: '.format(i)))
    if numero % 2 == 0:
        soma = numero + soma
        cont = cont + 1
print('Voce informou {} numeros pares e a soma foi {}'.format(cont, soma))

