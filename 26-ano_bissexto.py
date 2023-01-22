n1 = int(input('digite o ano: '))
if n1%4==0 and n1%100!=0 or n1%400==0:
     print('o ano {} é bissexto'.format(n1))
else:
     print('o ano {} não é bissexto'.format(n1))

