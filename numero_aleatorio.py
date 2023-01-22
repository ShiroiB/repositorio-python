import random
n1 = int(input('digite um numero de 0 a 5: '))
n2 = random.randrange(7)
if n1==n2:
         print('vc tirou o mesmo numero que o pc')
         print('voce = {} pc = {}'.format(n1,n2))
else:
         print('voce = {} pc = {}'.format(n1,n2))
         print('Nao foi desta fez')
