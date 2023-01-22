n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))
lista=[n1,n2,n3]
num=min(lista)
num2=max(lista)
print('seus numeros ordenados sao {}'.format(sorted(lista)))
print('o menor numero e {} e o maior numero e{}'.format(num,num2))
