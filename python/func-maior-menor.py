flag = False
lista1 = []

while not flag:
    lista1.append(int(input("insira um num: ")))
    if len(lista1) >=5:
        flag =True

def maior_list(l1):
    var1 = l1[0]
    for i in range(len(l1)):
        if l1[i] > var1:
            var1 = l1[i]
    return var1

def menor_list(l1):
    var2 = l1[0]
    for i in range(len(l1)):
        if l1[i] < var2:
            var2 = l1[i]
    return var2


maior = maior_list(lista1)
menor = menor_list(lista1)
print("o maior num é {} e o menor é {}".format(maior,menor))
lista1.sort()
print("a lista ordenada é:\n" +str(lista1))
print("o total de elementos é "+str(len(lista1)))
lista1.reverse()
print("a lista reversa é:\n" +str(lista1))


