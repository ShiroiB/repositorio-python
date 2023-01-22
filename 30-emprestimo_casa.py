n1 = float(input('qual e o valor da casa? '))
n2 = float(input('qual e o salario do comprador? '))
n3 = int(input('quantos anos de financiamento? '))
sal= n1/(n3*12)
cal=n2*0.30
if sal>cal:
     print('A casa que custa {:.2f} em {}, a prestação será de R${:.2f}'.format(n1,n3,sal))
     print('emprestimo reprovado!!!')
else:
     print('A casa que custa {:.2f} em {}, a prestação será de R${:.2f}'.format(n1,n3,sal))
     print('emprestimo aprovado!!!')
