import math
var_1 = int(input("informe um valor inteiro de 3 dígitos: "))
invertido = 0
while var_1>0:
    invertido = invertido*10+var_1%10
    var_1 = var_1/10
print(invertido)