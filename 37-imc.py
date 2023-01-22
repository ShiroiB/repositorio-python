n1=float(input('digite seu peso(Kg): '))
n2=float(input('digite a sua altura: '))
imc= n1/(n2*n2)
print('Seu imc é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <imc< 25:
    print('Peso ideal')
elif 25<imc<30:
    print('Sobrepeso')
elif 30<imc<40:
    print('Obesidade')
else:
     print('Obesidade Mórbida')
