''' faça um programa que leia uma frase pelo teclado e mostre: '''
'''- quantas vezes aparece a letra A '''
'''- em que posição ela aparece a primeira vez '''
'''- em que posição ela parece a ultima vez '''

'''
a = str(input('Digite seu Nome Completo: ').strip().lower())
print('a letra A aparece {} vezes'.format(a.count('a')))
print('a primeira letra A apareceu na posição {}'.format(a.find('a')+1))
print('a ultima letra A apareceu na posição {}'.format(a.rfind('a')+1))
'''

nome = str(input('Digite seu nome: '))

print('A letra -A- aparece {} vezes no seu nome'.format(nome.count('a')))
print('A letra -A- aparece na posicão {} a primeira vez'.format(nome.find('a')))
print('A letra -A- aparece na posição {} na ultima vez'.format(nome.rfind('a')))

