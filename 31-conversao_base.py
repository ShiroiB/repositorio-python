n1 = int(input('escreva um numero: '))
print(
''' digite um dos numeros abaixo\n
[1]converter para binario\n
[2]converter para octal\n 
[3]converter para hexadecimal''')
n2 = int(input('sua opcao e '))
if n2==1:
     n3 = bin(n1)
     print(' seu numero convertido em binario e de {}'.format(n3))
elif n2==2:
     n3 = oct(n1)
     print(' seu numero convertido em octal e de {}'.format(n3))
else:
    n3 = hex(n1)
    print(' seu numero convertido em hexadecimal e de{}'.format(n3))
