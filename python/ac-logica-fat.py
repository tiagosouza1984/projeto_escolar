
n1 = int(input('Digite a qtde de números: '))
for x in range(n1):
    n2 = int(input('Digite um número inteiro: '))
    fat = 1
    s =''
    for y in range(n2,0,-1):
        fat *= y
        if y == n2:
            s += str(y)
        else:
            s += ' * ' + str(y)
            print(" {} = {}".format(s,fat))
    
        
   