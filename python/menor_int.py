N1 = int(input("Número 1: "))
N2 = int(input("Número 2: "))
N3 = int(input("Número 3: "))

if N1 < N2 and N3:
    menor = N1
else:
    if N2 < N3:
        menor = N2
    else:
        menor = N3
print(menor)

    