def main():
    def printMatriz(matriz):
        
        tabuleiro = "{} | {} | {}\n__ __ __\n{}|{}|{}\n{}|{}|{}".format(matriz[0], matriz[1], matriz[2], matriz[3], matriz[4], matriz[5], matriz[6], matriz[7], matriz[8])
        print(tabuleiro)

    def avalTermino(matriz, jogadorAtu, marcaAtu):

        if (matriz[0] == marcaAtu and matriz[1] == marcaAtu and matriz[2] == marcaAtu) or \
            (matriz[3] == marcaAtu and matriz[4] == marcaAtu and matriz[5] == marcaAtu) or \
            (matriz[6] == marcaAtu and matriz[7] == marcaAtu and matriz[8] == marcaAtu) or \
            (matriz[0] == marcaAtu and matriz[3] == marcaAtu and matriz[6] == marcaAtu) or \
            (matriz[1] == marcaAtu and matriz[4] == marcaAtu and matriz[7] == marcaAtu) or \
            (matriz[2] == marcaAtu and matriz[5] == marcaAtu and matriz[8] == marcaAtu) or \
            (matriz[0] == marcaAtu and matriz[4] == marcaAtu and matriz[8] == marcaAtu) or \
            (matriz[2] == marcaAtu and matriz[4] == marcaAtu and matriz[6] == marcaAtu):
            
            printMatriz(matriz)
            print("O jogador ", jogadorAtu, " é o vencedor!!!")
            return True
        elif (matriz.count("X") + matriz.count("O") == 9):
            printMatriz(matriz)
            print("Fim de jogo. Empate!")
            return True
        else:
            return False
        

    matriz = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    continua = True
    jogadorAtu = "1"
    marcaAtu = "X"

    while continua:
        printMatriz(matriz)
        pos = int(input("Jogador " + jogadorAtu + " faça sua jogada: "))

        while matriz[pos-1] == "X" or matriz[pos-1] == "O" or not(pos >= 1 and pos <= 9):
            pos = int(input("Casa já ocupada ou invalida, refaça a jogada:"))

        matriz[pos-1] = marcaAtu

        if avalTermino(matriz, jogadorAtu, marcaAtu):
            continua = False
        else:
            if jogadorAtu == "1":
                jogadorAtu = "2"
                marcaAtu = "O"            
            else:
                jogadorAtu = "1"
                marcaAtu = "X"   
if __name__ == "__main__":
    main()