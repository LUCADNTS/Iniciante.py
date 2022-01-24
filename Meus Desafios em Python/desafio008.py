'''escreva um progrma que leia o valor em metros e o exiba convertido em centimetros e milimetros '''

metros = float(input('Digite quantos metros: '))

centimetros = metros * 100
milimetros = metros * 1000

print('{:.2f} Metros tem {:.2f} Centimetros e tem {:.2f} Milimetros'.format(metros, centimetros, milimetros))
