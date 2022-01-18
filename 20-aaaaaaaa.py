n1 =str(input('digite o nome: ')).upper().strip()
n2 = n1.count('A')
n3 = (n1.find('A')+1)
n4 = (n1.rfind('A')+1)
print("o nome tem {} de A, a primeira posicao fica no {} e a ultima fica 
{}".format(n2,n3,n4))
