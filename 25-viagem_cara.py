n1 = float(input('digite a distancia da viagem: '))
if n1<=200:
     preço = n1 *0.50
     print('O preço da passagem será de R$ {:.2f}'.format(preço))

else:
     preço = n1 *0.45
     print('O preço da passagem será de R$ {:.2f}'.format(preço))
