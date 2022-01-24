''' 
REFAÇA O DESAFIO 035 do triangulos, acrescentando o recurdo de mostrar que tipo de triangulo sera formado:
- equilatero: todos os lados iguais
- isosceles: dois lados iguais
- escaleno: todos os lador diferentes
'''

r1 = int(input('reta 1: '))
r2 = int(input('reta 2: '))
r3 = int(input('reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses seguimentos forman um triangulo ', end='')
    if r1 == r2 and r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os seguimentos não podem formar um triangulo')
