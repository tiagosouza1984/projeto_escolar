

flag = False
wrong_letter =[]
list_letter =[]
count = 0
word = input("Digite a palavra a ser adivinhada: ")
word = word.upper()

#função que recebe a palavra, checa o tamanho da string imprime o tamanho em lista com os símbolos e retorna a lista
def print_forca(palavra):
    symbol_forca =[]
    for x in range(len(palavra)):
        #adiciona a lista symbol_forca o simbolo "_" 
        symbol_forca.append('_')
    print("A palavra é "," ".join(symbol_forca))
    return symbol_forca

#função que checa se a letra digitada está contida na palavra
def print_letter(letra):
    count_a = 0
    #checa se o último elemento da lista está contido na palavra
    if letra[-1] in word:
        #executa a repetição pelo número de indices da palavra, checando cada índice da palavra
        for i in range (len(word)):  
            #checa o último elemento inserido na lista e procura se é igual a letra no índice palavra        
            if letra[-1] == word[i]:
                #a variável get_symbol que recebeu a lista com os símbolos e se tornou uma lista recebe a letra digitada no indice conforme o laço for
                get_symbol[i] = letra[-1] 
        print("A palavra é "," ".join(get_symbol))         
    else:
        #caso letra digitada não estiver contida na lista imprime o que já está contido em get_symbol
        print("A palavra é "," ".join(get_symbol)) 
        wrong_letter.append(input_letter)
        #imprime a lista com as letras erradas
        print('Letras erradas '," ".join(wrong_letter))
        count_a +=1
    return count_a
    
#função que define o fim do programa        
def check_end(simbolos, contador):
    flag_end = False
    #verifica quantos elementos "_" restam na lista getl_symbol
    if simbolos.count("_") == 0:
        print("Parabéns! Você ganhou! A palavra é: ",word)
        flag_end = True
    #verifica se count já acumulou o número de tentativas erradas 
    if contador == 7:
        print("Que pena! Você perdeu! A palavra é: ",word)
        flag_end = True
    return flag_end

#variável que chama a função print_forca e recebe como retorno os símbolos em lista no lugar da palavra enviada por parâmetro
get_symbol = print_forca(word)

while not flag:
    input_letter = input("Digite uma letra: ")
    input_letter = input_letter.upper()
    #checa se a letra digitada ainda não foi tentada pelo usuário
    if not input_letter in list_letter:
        #guarda a letra digitada pelo usuário em uma lista
        list_letter.append(input_letter)
        #váriável que chama função print_letter imprimindo a letra digitada  e retornando apenas o contador icrementando, em caso de letra incorreta
        count += print_letter(list_letter)         
    else:
        print('Palpite repetido!')
    #variável que chama a função check_end enviando os get_symbol e count por parametro e devolvendo true caso programa chegue ao fim
    flag = check_end(get_symbol, count)
