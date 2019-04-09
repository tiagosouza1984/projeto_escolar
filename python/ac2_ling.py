import math
'''

Faça um programa que receba um número N, que seja inteiro e positivo não nulo, e exiba os seguintes valores:

i) o quadrado de N;
ii) a raiz quadrada de N;
iii) a raiz cúbica de N;
iv) o número pi divido por N;
v) o produto do número de Euler e N;
vi) o logaritmo de N na base 7;
vii) o logaritmo de N na base 10;
viii) o logaritmo natural de N;
ix) a exponencial de N na base e
'''
n1 = float(input("insira um numero: "))
quad = n1**2
raiz = math.sqrt(n1)
cub =  n1**(1/3)
pi_N1 = 3.14/n1
eN1 = 2.718*n1
log7N1 = math.log(n1, 7)
log10N1 = math.log(n1, 10)
logN1 = math.log(n1, math.e)
exN1 = math.exp(n1)
print(quad)
print(raiz)
print(cub)
print(pi_N1)
print(eN1)9
print(log7N1)
print(log10N1)
print(logN1)
print(exN1)