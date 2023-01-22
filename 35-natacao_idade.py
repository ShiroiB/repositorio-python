n1= float(input('digite o ano de nascimento: '))
n2= float(input('digite o ano atual: '))
s = n2 - n1
if s<=9:
    print('Vc possui {} anos\n Sua categoria e MIRIM'.format(s))
elif s<=14:
    print('Vc possui {} anos\n Sua categoria eINFANTIL'.format(s))
elif s<=19:
    print('Vc possui {} anos\n Sua categoria e JUNIOR'.format(s))
elif s<=25:
     print('Vc possui {} anos\n Sua categoria e SENIOR'.format(s))
else:
    print('Vc possui {} anos\n Sua categoria e MASTER'.format(s))
