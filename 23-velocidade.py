n1 = float(input('digite a velocidade do seu carro: '))
multa = float
multta02 = float
if n1<=80:
     print('sua velocidade esta no limite permitido')
else:
     multa = n1 - 80
     multa02 = multa * 7.00
     print('Sua velocidade esta acima do permitido, a multa e de R${:.2f}'.format(multa02))
