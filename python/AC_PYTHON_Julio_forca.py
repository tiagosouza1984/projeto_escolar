def criaResp(palavra):

	resposta = []	
	lRespAtual = []

	for x in palavra:
		resposta.append(x)
		lRespAtual.append("_")

	return resposta, lRespAtual, palavra

def printBoneco(partB, lRespAtual):
	
	respAtu = ""
	strBoneco = "    ________\n   |        |\n   |        {}\n   |       {}{}{}\n   |        {}\n   |       {} {}\n   |\n__/|\__"
	
	print(strBoneco.format(partB[0][1],partB[2][1],partB[1][1],partB[3][1],partB[4][1],partB[5][1],partB[6][1]))

	"""for x in lRespAtual:
		respAtu += x + " "
	print("A palavra é:",respAtu)"""

def avalLetra(letra, resposta, lRespAtual):

	acertou = False
	contador = 0

	for x in resposta:
		if letra == x:
			lRespAtual[contador] = letra
			acertou = True
		contador += 1	

	return acertou, lRespAtual

def avalTermino(lRespAtual):

	terminou = True

	for x in lRespAtual:
		if x == "_":
			terminou = False

	return terminou

resposta, lRespAtual, palavra = criaResp(input("Digite a palavra a ser adivinhada: "))
partB = [["O",""],["|",""],["/"," "],["\ ",""],["|",""],["/",""],["\ ",""]]
parteAtu = 0
continua = True
respFim = ""
chance = 1
erradas = []
print(resposta, lRespAtual, palavra)

while continua:
	printBoneco(partB, lRespAtual) 
	
	if len(erradas) > 0:
		print("Letras erradas:", erradas)	
	if chance > 7:
		print("A palavra era:", palavra)
		continua = False
	elif avalTermino(lRespAtual):
		continua = False	
	else:
		letra = input("Digite uma letra: ")

		while letra in erradas or letra in lRespAtual:
			print("Palpite repetido!")
			letra = input("Digite uma letra: ")
		acertou, lRespAtual = avalLetra(letra, resposta, lRespAtual)

		if not acertou:
			erradas.append(letra)
			partB[parteAtu][1] = partB[parteAtu][0]
			parteAtu += 1
			chance += 1