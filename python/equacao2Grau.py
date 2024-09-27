import math
n1 = int(input("insira o 1o valor: "))
n2 = int(input("insira o 2o valor: "))
n3 = int(input("insira o 3o valor: "))

if n1 == 0:
    print("não é uma equação de segundo grau!")
    SystemExit

delta = (n2**2) - (4 * n1)*n3 
if delta < 0:
    print("não existem raízes reais")
    print(delta)
elif delta == 0:
    x = - n2 + (math.sqrt(delta/(2*n1)))
    print("a equação possui apenas uma raiz que é "+ str("x"))
elif delta > 0:
    x1 = - n2 + (math.sqrt(delta/(2*n1)))
    x2 = - n2 + (math.sqrt(delta/(2*n1)))

