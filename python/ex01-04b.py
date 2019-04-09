"""
mentira = bool(input())
verdade = bool(input())

if not mentira or verdade:
    print(not mentira)
else:
    if not mentira and verdade:
        print(not verdade)
    else:
        print(mentira or verdade)

x = 7
y = 10
resposta = x < 7
if resposta:
    print("x é menor que y")
else:
    print("x não é maior que y")

resposta = float(input("digite a nota: "))
if resposta < 6:
    print("nota F")
elif resposta < 7:
    print("nota D")
elif resposta < 8:
    print("nota c")
elif resposta < 9:
    print("nota B")
else:
    print("nota A")

num =int(input("digite um número inteiro: "))
if num > 10 and num < 20:
    print("número dentro do intervalo")
elif num <= 10:
    print("número abaixo do intervalo")
else:
    print("número acima do intervalo")

nota = float(input("digite a nota: "))
if nota > 9:
    print("aprovado com louvor")
elif nota >= 6:
    print("aprovado")
elif nota >= 4:
    print("recuperação")
else:
    print("reprovado")
"""

n1 = 25
n2 = 10
a= 0
b=0
c=0
d=0
resultado = 0
opcao = input("digite a opção: a, b, c, ou d: ")
if opcao == 'a':
    resultado = n1+n2
if opcao == 'b':
    resultado = n1-n2
if opcao == 'c':
    resultado = n1*n2
if opcao == 'd':
    resultado = n1/n2
if opcao != a and b and c and d:
    print("opção inválida")
    
print(resultado)