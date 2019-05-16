
Vlista = []
flag = False

while not flag:
    Vlista.append(int(input("insira um número: ")))
    if len(Vlista) >= 5:
        Vnum = int(input("insira um número para comparação: "))
        flag = True

def compare_num(lista, n1):
    #print(lista.count(n1)) (conta quantas vezes n1 aparece na lista)
    count = 0
    for i in range(len(lista)):
        if lista[i] == n1:
            count+= 1
   
    print("O valor {} aparece {} vezes na lista".format(n1,count))

def existe(lista,n1):
    for i in range(len(lista)):
        if n1 == lista[i]:
            print("{} está na lista".format(n1))

compare_num(Vlista,Vnum)
existe(Vlista,Vnum)