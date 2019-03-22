V_apples = int(input("Informe o total de maçãs da compra: "))
if V_apples < 12:
    V_preco = 1.30
    V_total = V_apples * V_preco
    print("O custo total da compra é de " +str(V_total)+ " R$")
else:
    if V_apples >= 12:
        V_preco = 1.00
        V_total = V_apples * V_preco
        print("O custo total da compra é de " +str(V_total)+ " R$")