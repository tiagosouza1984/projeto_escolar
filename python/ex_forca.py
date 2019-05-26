word = input("Digite a palavra a ser adivinhada: ")
word = word.upper()
wrong_letter =[]
list_letter =[]
count = 0
flag = False

#função que recebe a palavra, checa o tamanho da string imprime o tamanho em lista com os símbolos e retorna a lista
def print_forca(palavra):
    symbol_forca =[]
    for x in range(len(palavra)):
        symbol_forca.append('_')
    print("A palavra é "," ".join(symbol_forca))
    return symbol_forca

#função que checa se a letra digitada está contida na palavra
def print_letter(letra, contador):
    #executa a repetição pelo número de indices da palavra, checando cada índice da palavra
    for i in range (len(word)):
        if letra[i] in word:  
            print("entrou")
            """
            for indice in range (len(word)):        
                if letra[indice] == word[indice]:
                    get_symbol[indice] = word[indice] 
                    print("A palavra é "," ".join(get_symbol))     
        else:
            print("A palavra é "," ".join(get_symbol)) 
            wrong_letter.append(input_letter)
            contador += 1
            print('Letras erradas '," ".join(wrong_letter))
            return contador
            """

def check_end(simbolos, contador):
    if simbolos.count("_") == 0:
        print("Parabéns! Você ganhou! A palavra é: ",word)
        flag = True 
    if contador == 7:
        print("Que pena! Você perdeu! A palavra é: ",word)
        return contador


get_symbol = print_forca(word)

while count < 7 and not flag:
    input_letter = input("Digite uma letra: ")
    input_letter = input_letter.upper()
    #checa se a letra digitada ainda não foi tentada pelo usuário
    if not input_letter in list_letter:
        #guarda a letra digitada pelo usuário em uma lista
        list_letter.append(input_letter)
        #chama função que imprime a letra digitada 
        print_letter(list_letter, count)           
    else:
        print('Palpite repetido!')
    
