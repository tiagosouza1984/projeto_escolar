word = input("Digite a palavra a ser adivinhada: ")
word = word.upper()
wrong_letter =[]
list_letter =[]

#função que recebe a palavra, checa o tamanho da string imprime o tamanho em lista com os símbolos e retorna a lista
def print_forca(palavra):
    symbol_forca =[]
    for x in range(len(palavra)):
        symbol_forca.append('_')
    print("A palavra é "," ".join(symbol_forca))
    return symbol_forca

get_symbol = print_forca(word)
count = 0
i=0
while count < 7:
    input_letter = input("Digite uma letra: ")
    input_letter = input_letter.upper()
    if not input_letter in list_letter:
        list_letter.append(input_letter)
        if list_letter[i] in word:
            for indice in range (len(word)):          
                if list_letter[i] == word[indice]:
                    get_symbol[indice] = word[indice] 
            print("A palavra é "," ".join(get_symbol))       
        else:
            print("A palavra é "," ".join(get_symbol)) 
            wrong_letter.append(input_letter)
            count += 1
            print('Letras erradas ',wrong_letter)
        i+=1         
    else:
        print('Palpite repetido!')
 #check apagar       
print(list_letter)
 

"""
def draw_forca(forca1, wrong1):
    var1 =" "  
    var2 =""
    flag = False
    for x in range(0,7): 
        if not flag:              
            for y in range(0,11):
                if y > 0:
                    var1 +="* "
                else:
                    var1 += "|\n"
            var1= var1[::-1]
            print(var1)
            flag = True
        var2 = "|"
       # print(var2)
    if wrong1 == "teste":
        var1+= "O"
       
forca = 1
wrong= "teste"
draw_forca(forca, wrong)
"""