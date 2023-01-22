n1 = float(input('digite seu salario: '))
if n1<=1250:
     salario = n1 * 15/100
     nova= salario + n1
     print('o reajuste foi de R${:.2f}, o seu salario atual e deR${:.2f}'.format(salario,nova))

else:
     salario = n1*10/100
     nova= salario + n1
     print('o reajuste foi de R${:.2f}, o seu salario atual e deR${:.2f}'.format(salario,nova))
