''' faça um programa que leia o nome completo de uma pessoa,
 mostrando em seguida o primeiro e o ultimo nome separadamente'''
'''ex: ana maria de souza
primeiro: ana
segundo: souza '''
'''
nome = str(input('Digite seu nome completo: ')).strip()
div = nome.split()
print('Prazer em te conhecer!!\nseu primeiro nome é: {}'.format(div[0]))
print('seu ultimo nome é: {}'.format(div[len(div)-1]))
'''

nome = str(input('digite seu nome completo:  ')).strip()
dividido = nome.split()

print('Prazer em te conhecer {} '.format(nome))

print('Seu primeiro nome é {}'.format(dividido[0]))

print('O seu ultimo nome é {}'.format(dividido[len(dividido)-1]))

