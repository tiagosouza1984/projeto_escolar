Valor_prod = float(input("Informe o valor de compra do produto: "))
if Valor_prod < 20:
    Valor_prod = Valor_prod+(Valor_prod*(45/100))
    print("O valor da venda será de " +str(Valor_prod))
else: 
    if Valor_prod >= 20:
        Valor_prod = Valor_prod+(Valor_prod*(30/100))
        print("O valor da venda será de " +str(Valor_prod))