
import math
n1 = float(input('digite um valor cateto oposto\n'))
n2 = float(input('digite um valor para o cateto adjacente\n'))
re = math.hypot(n1,n2)
print('a hipotenusa vai medir {:.2f}'.format(re))
