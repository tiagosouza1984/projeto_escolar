N1 = int(input("Número 1: "))
N2 = int(input("Número 2: "))
N3 = int(input("Número 3: "))

if N1 < (N2 and N3):
    menor = N1
else:
    if N2 < N3:
        menor = N2
    else:
        menor = N3

##segundo valor
 
if menor == N1:
    if N2 < N3:
        inter = N2
        fim = N3
    else:
        inter = N3
        fim = N2
else:
    if menor == N2:
        if N1 < N3:
            inter = N1
            fim = N3
        else:
            inter = N3
            fim = N1
    else:
        if menor == N3:
            if N1 < N2:
                inter = N1
                fim = N2
            else:
                inter = N2
                fim = N1
        
               
print(menor)
print(inter)
print(fim)
