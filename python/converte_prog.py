var_reais = float(input("informe o valor reservado p/ viagem em reais: "))
var_dolar = float(input("informe a cotação do dolar de hoje: "))
var_total = var_reais * var_dolar
print("você tem "+str(var_total)+" dólares disponíveis para viagem")