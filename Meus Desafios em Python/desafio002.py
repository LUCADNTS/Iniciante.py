'''faça um programa que leia a mensagem de uma pessoa e mostre uma mensagem de boas vindas'''

nome = input('digite seu nome: \n')
print('Prazer em te conhecer', nome)

altura = float(input('Qual sea altura? \n'))
if(altura >= 1.85):
    print('Nossa, voce é bem alto em !')
else:
    print('legal')
idade = int(input('qual sua idade?\n'))
if(idade <= 30 ):
    print("Nossa, Você é bem jovem.")
else:
    print("Voce ja esta velhor")


