n1= float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
s= (n1+n2)/2
if s<5.0:
    print('Sua nota foi {:.1f}, ESTA REPROVADO'.format(s))
elif 5<=s<7:
     print('Sua nota foi {:.1f}, RECUPERAÇÃO'.format(s))
else:
     print('Sua nota foi {:.1f}, ESTA APROVADO'.format(s))
