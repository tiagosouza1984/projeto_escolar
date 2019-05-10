count = 0
Vlista = []
flag = False

while not flag:
    Vlista.append(int(input("insira um número: ")))
    if len(Vlista) >= 5:
        Vnum = int(input("insira um número para comparação: "))
        flag = True

resposta = compare_num(Vlista, Vnum)

def compare_num(lista, n1):
    for i in range(len(lista)):
        if lista[i] == n1:
            count+=1
    print("O valor {} aparece {} na lista".format(n1,count))