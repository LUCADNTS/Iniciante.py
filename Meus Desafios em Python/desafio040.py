''' crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5.0: REPROVADO
- média entre 5.0 e 6.9: RECUPERAÇÃO
- média 7.0 ou superior: APROVADO!
'''

nota1 = float(input('Digite a Primeira Nota: '))
nota2 = float(input('Digite a Segunda Nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('\033[1;31;40m VOCE TEVE UMA MÉDIA DE {} VOCE FOI REPROVADO ! \033[m'.format(media))
    print('\033[1;31;40m SE ESFORCE E ESTUDE MAIS NO PROXIMO ANO !!\033[m')

elif media >= 5.0 and media <= 6.9:
    print('\033[1;33;40m VOCE TEVE UMA MÉDIA DE {} E ESTA DE RECUPERAÇÃO !\033[m'.format(media))
    print('\033[1;33;40m ESTUDE MAIS !! \033[m')

else:
    print('\033[1;32;40m VOCE TEVE UMA MÉDIA DE {} E FOI APROVADO !\033[m'.format(media))
    print('\033[1;32;40m PARABENS !!\033[m')
