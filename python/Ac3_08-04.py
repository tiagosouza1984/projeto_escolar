# Caso feito em dupla, coloque os nomes aqui:
# nome1:
# nome2:

# Este exercício é sobre o uso da estrutura de seleção (if),
# portanto NÃO é para ser usado laço de repetição (while)

# Não digite nenhum texto para pedir o dado de entrada para o usuário

# Imprima a saída exatamente como mostrado nos exemplos do enunciado,
# qualquer espaço em branco a mais ou caractere diferente resultará em erro
# nos testes e será descontado da nota do exercício.
value = float(input())

if value > 0 and value <= 1000000.00:
    if value >= 100:
        N100 = value//100
        value = round(value%100, 2)
        print(str(int(N100))+" nota(s) de R$ 100.00")
    if value >= 50 and value < 100:
        N50 = value//50
        value = round(value%50, 2)
        print(str(int(N50))+" nota(s) de R$ 50.00")
    if value >= 20 and value < 50:
        N20 = value//20
        value = round(value%20, 2)
        print(str(int(N20))+" nota(s) de R$ 20.00")
    if value >= 10 and value < 20:
        N10 = value//10
        value = round(value%10, 2)
        print(str(int(N10))+" nota(s) de R$ 10.00") 
    if value >= 5 and value < 10:
        N5 = value//5
        value = round(value%5, 2)
        print(str(int(N5))+" nota(s) de R$ 5.00")
    if value >= 2 and value < 5:
        N2 = value//2
        value = round(value%2, 2)
        print(str(int(N2))+" nota(s) de R$ 2.00") 
    if value >= 1 and value < 2:
        N1 = value//1
        value = round(value%1, 2)
        print(str(int(N1))+" moeda(s) de R$ 1.00") 
    if value >= 0.50 and value < 1:
        N0_50 = value//0.50
        value = round(value%0.50, 2)
        print(str(int(N0_50))+" moeda(s) de R$ 0.50")
    if value >= 0.25 and value < 0.50:
        N0_25 = value//0.25
        value = round(value%0.25, 2)
        print(str(int(N0_25))+" moeda(s) de R$ 0.25")
    if value >= 0.10 and value < 0.25:
        N0_10 = value//0.10
        value = round(value%0.10, 2)
        print(str(int(N0_10))+" moeda(s) de R$ 0.10")
    if value >= 0.05 and value < 0.10:
        N0_05 = value//0.05
        value = round(value%0.05, 2)
        print(str(int(N0_05))+" moeda(s) de R$ 0.05")
    if value >= 0.01 and value < 0.05:
        N0_01 = value/0.01
        print(str(int(N0_01))+" moeda(s) de R$ 0.01")
