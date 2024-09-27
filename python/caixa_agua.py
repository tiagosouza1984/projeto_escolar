var_sal = float(input("informe o valor do salário mínimo: "))
var_consumo = float(input("informe o valor do consumo mensal"))
var_mil_L = var_sal*2/100
var_preco_L = var_mil_L/1000
var_bill = var_consumo*var_preco_L
var_total = var_bill * 85/100
print(var_mil_L)
print(var_preco_L)
print(var_bill)
print(var_total)
