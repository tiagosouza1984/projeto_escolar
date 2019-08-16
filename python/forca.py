# função que recebe a palavra e retorna os símbolos
def func_palavra(palavra):
    symbol_forca = []
    for x in range(len(palavra)):
        # adiciona a lista symbol_forca o simbolo "_"
        symbol_forca.append('_')
    return symbol_forca


'''
função que recebe a palavra, checa o tamanho da string
imprime o tamanho em lista com os símbolos e retorna a lista
'''


def print_forca(palavra, partB, simbolo, letra_errada):
    # variável tipo string com o desenho da forca e espaços para o boneco
    boneco = "    ________\n   |        |\n   |        {}\n   |       {}{}{}\n   |        {}\n   |       {} {}\n   |\n__/|\__"
    '''
    print da forca com as partes do boneco armazenados
    como matriz em partB[][]
    '''
    print(boneco.format(partB[0][1], partB[2][1], partB[1][1], partB[3][1], partB[4][1], partB[5][1], partB[6][1]))
    print("A palavra é ", " ".join(simbolo))
    '''
    verifica se a quantidade de itens da lista é diferente de
    vazia para imprimir a lista com as letras erradas
    '''
    if len(letra_errada) != 0:
        # imprime a lista com as letras erradas
        print('Letras erradas ', " ".join(letra_errada))
    return partB, simbolo, letra_errada

# função que checa se a letra digitada está contida na palavra


def print_letter(palavra, letra, simbolo, partB, contador, letra_errada):
    # checa se o último elemento da lista está contido na palavra
    if letra[-1] in palavra:
        '''
        executa a repetição pelo número de indices da
        palavra, checando cada índice da palavra
        '''
        for i in range(len(palavra)):
            '''
            checa o último elemento inserido na
            lista e procura se é igual a letra no índice palavra
            '''
            if letra[-1] == palavra[i]:
                '''
                a variável get_symbol que recebeu a lista com os
                símbolos e se tornou uma lista recebe a letra digitada no indice conforme o laço for
                '''
                simbolo[i] = letra[-1]
    else:
        '''
        caso letra digitada não estiver contida na lista
        imprime o que já está contido em get_symbol
        '''
        partB[contador][1] = partB[contador][0]
        # adiciona a letra errada a lista wrong_letter
        letra_errada.append(letra[-1])
        contador = contador+1
    # retorna para o contador que irá icrementar a cada erro
    return letra, simbolo, partB, contador, letra_errada

# função que define o fim do programa


def check_end(flag_end, palavra, simbolos, imprime_forca):
    # verifica quantos elementos "_" restam na lista getl_symbol
    if simbolos.count("_") == 0:
        print("Parabéns! Você ganhou! A palavra é: ", palavra, "\n")
        flag_end = True
    return flag_end


def main():
    flag = False
    wrong_letter = []
    list_letter = []
    MypartB = [["O", ""], ["|", ""], ["/", " "], ["\ ", ""], ["|", ""], ["/", ""], ["\ ", ""]]
    count = 0
    word = input("Digite a palavra a ser adivinhada: ")
    word = word.upper()

    # variável que chama a função palavra e recebe como retorno os símbolos em lista no lugar da palavra enviada por parâmetro
    get_symbol = func_palavra(word)

    # verifica condição de flag não ativada enquanto ela for menor que 7 tentativas erradas
    while not flag:
        # chama função que imprime a forca atualizada com os simbolos de get_symbol e
        MypartB, get_symbol, wrong_letter = print_forca(
            word, MypartB, get_symbol, wrong_letter
        )
        input_letter = input("Digite uma letra: ")
        # deixa todos os caracteres maiúsculos
        input_letter = input_letter.upper()
        # checa se a letra digitada ainda não foi tentada pelo usuário
        if input_letter not in list_letter:
            # guarda a letra digitada pelo usuário em uma lista
            list_letter.append(input_letter)
            '''
            váriável que chama função print_letter imprimindo a letra digitada
            e retornando apenas o valor a variável icrementado, em caso de letra incorreta
            '''
            list_letter, get_symbol, MypartB, count, wrong_letter = print_letter(
                word, list_letter, get_symbol, MypartB, count, wrong_letter
            )
        else:
            print('Palpite repetido!')
        # variável que chama a função check_end enviando os get_symbol e count por parametro e devolvendo true caso programa chegue ao fim
        flag = check_end(flag, word, get_symbol, print_forca)
        # verifica se count já acumulou o número de tentativas erradas
        if count == 7:
            # imprime a forca pela ultima vez
            MypartB, get_symbol, wrong_letter = print_forca(word, MypartB, get_symbol, wrong_letter)
            print("Que pena! Você perdeu! A palavra é: ", word, "\n")
            flag = True


if __name__ == "__main__":
    main()
