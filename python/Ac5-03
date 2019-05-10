#Nomes caso feito em duplas:
#Nome1:Tiago da Silva Souza
#Nome2:Brenda Macedo de Oliveira

selo_value = float(input())
flag = False
selo_50 = 0
selo_20 = 0

while not flag:
  if not((selo_value*10) % 1 == 0) or selo_value < 0.70 or selo_value > 6.20:
    print("Preço inválido, refaça a leitura do pacote.")
    selo_value = float(input())
  else:
    flag = True
   
while selo_value > 0:
  if selo_value % 0.50 == 0:
    selo_value = round(selo_value - 0.50,1)
    selo_50 += 1
  else:
    selo_20 += 1
    selo_value = round(selo_value - 0.20,1)
print("Compre {} selo(s) de R$ 0.50 e {} selo(s) de R$ 0.20!".format(selo_50,selo_20))