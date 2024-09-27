# Nomes caso feito em duplas:
#Nome1:Tiago da Silva Souza
#Nome2:Brenda Macedo de Oliveira
n1 = int(input(""))
n2 = int(input(""))
flag = False
count = 1
#checa inteiros n1 e n2 entre 1 e 9.
for x in range (n1,n2):
  print("Tabuada do {}:".format(n1))
  for x in range(1,10):
    tab1=count*n1
    print("{} x {} = {}".format(n1,count,tab1))
    count+=1
  count = 1
  n1+=1



  
