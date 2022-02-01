'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa, mostre:
- A media de idade do grupo.
- qual é o nome do homem mais velho
- quantas mulheres tem menos de 20 anos.
'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for c in range(1, 5):
    print('--------[{}ªPessoa]--------'.format(c))
    nome = str(input('Digite o Nome: '))
    idade = int(input('Digite a Idade: '))
    sexo = str(input('M/F :')).upper()
    somaidade = somaidade + idade
    if c == 1 and sexo in 'mM':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'fF' and idade < 20:
        totmulher20 = totmulher20 + 1

mediaidade = somaidade / 4
print('A media de idade essas pessoas é {}'.format(mediaidade))
print('O Homem mais velho tem {} e o seu nome é {}'.format(maioridadehomem, nomevelho))
print('Tem {} mulher(es) com menos de 20 Anos'.format(totmulher20))
