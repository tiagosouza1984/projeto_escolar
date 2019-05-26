
flag_input = False
flag_range = False
linha = []

"""
player1 = int(input("player1 escolha a posição desejada de 1 a 9: "))


player2 = int(input("player2 escolha a posição desejada de 1 a 9: "))
"""



linha = ['12', '00', '20']

for i in range(3):
    for j in range(3):
        posicao = str(i) + str(j)

        if posicao in linha:
            print("x", end='', flush=True)
        elif i < 2:
            print("_", end='', flush=True)
        else:
            print(" ", end='', flush=True)

        if j < 2:
            print(" | ", end='', flush=True)
    print("")
        
