n1 = float(input('digite seu numero: '))
n2 = float(input('digite seu numero: '))
n3 = float(input('digite seu numero: '))
if (n2 - n3) < n1 < n2 + n3 and (n1 - n3) < n2 < n1 + n3 and ( n1 - n2 ) < n3 < n1 + n2:
    print('Forma um triangulo!!!!')
else:
    print('Não forma um triangulo')
    
    
