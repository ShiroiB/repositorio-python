n1 = int(input('digite um o ano do seu nascimento: '))
n2 = int(input('digite um o ano atual: '))
cal = n2 - n1
print('vc tem {} anos'.format(cal))
if cal<18:
    print('Faltam {} anos para se alistar'.format(18-cal))
elif cal==18:
    print('Voce tem que se alistar')
else:
    print('Voce ja passou da idade de se alistar') 
