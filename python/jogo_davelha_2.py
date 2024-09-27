"""
player1 = int(input("player1 escolha a posição desejada de 1 a 9: "))
player2 = int(input("player21 escolha a posição desejada de 1 a 9: "))
"""
linha = [1,6,9]

for i in range(1,10):
#se i estiver na lista linha imprime x ou o com end concatenando o print na mesma linha
    if i in linha:
        print("x", end='')
    if i < 7:
        print("_", end='')
    else:
        print(" ", end='')

    
    
    #no range de 1 a 10 imprime vazio e quebra a linha nos multiplos de 3, para os demais imprime a barra |    
    if i % 3 == 0:
        print("")
    else:
        print("|", end='')