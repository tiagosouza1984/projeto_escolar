''' Nome e RA dos alunos caso feito em dupla
aluno1:
aluno2:

'''
import math
###########
# O código para receber o valor da área já está dado:
area = int(input())

###########
# Começe a resolução do seu código a partir daqui:

# regra de 3 -> se 5m = 1L, area = xL
total_litros  = area*1/5

# Digite abaixo o código referente à resolução do item a)
#quantas vezes 18L existem dentro de total_litros
N1 = float(total_litros)/18
N1 = math.ceil(N1)
C1 = float(N1)*85
print( "a) Latas de 18l: "+str(N1)+ " Custo: R$ {:.2f}" .format(C1))

'''
formatação do texto do print - item a)
a) Latas de 18l: N1 Custo: R$ C1
onde N1 é o número de latas de 18 litros, formatado como inteiro
e C1 é o custo total no caso a), formatado como float com 2 casas decimais
'''

###########
# Digite abaixo o código referente à resolução do item b)
#quantas vezes 3.6L existem dentro de total_litros
N2 = float(total_litros)/3.6
N2 = math.ceil(N2)
C2 = float(N2)*23
print("b) Latas de 3.6l: "+str(N2)+ " Custo: R$ {:.2f}" .format(C2))

"""

formatação do texto do print - item b)
a) Latas de 3.6l: N2 Custo: R$ C2
onde N2 é o número de latas de 3.6 litros, formatado como inteiro
e C2 é o custo total no caso b), formatado como float com 2 casas decimais

"""
###########
# Digite abaixo o código referente à resolução do item c)
#quantas vezes 18l existe dentro de total_litros
N1_c = float(total_litros) /18
#arredende N1_c para menor ou igual inteiro
N1_c = math.floor(N1_c)
#resto da divisão de N1_c por 18
resto_N1_c = float(total_litros) %18
#quantas vezes 3.6l existem dentro do resto da divisão de N1_c por 18
N2_c = math.ceil(resto_N1_c)/3.6
#arredonde N2_c para maior ou igual inteiro
N2_c = math.ceil(N2_c)
#soma dos totais de N1_c e N2_c multiplicados por seus respectivos preços
C3 = (N1_c*85)+(N2_c*23)
print ("c) Latas de 18l: "+str(N1_c)+" Latas de 3.6l: " +str(N2_c)+ " Custo: R$ {:.2f}" .format(C3))



'''
formatação do texto do print - item c)
a) Latas de 18l: N1_c Latas de 3.6l: N2_c Custo: R$ C3
onde N1_c é o número de latas de 18l no caso c), formatado como inteiro
onde N2_c é o número de latas de 3.6l no caso c), formatado como inteiro
e C3 é o custo total no caso c), formatado como float com 2 casas decimais
'''
###########