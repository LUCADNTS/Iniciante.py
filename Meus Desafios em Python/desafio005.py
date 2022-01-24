''' faça um programa que leia e mostre na tela o seu secussor e seu antecessor'''
num = int(input('Digite um numero: '))

antecessor = num - 1
sucessor = num + 1

print('O antecessor de {} é {}'.format(num, antecessor))
print('O sucessor de {} é {}'.format(num, sucessor))
