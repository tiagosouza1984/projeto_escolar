quant_km = float(input("insira os km's percorridos por seu carro: "))
quant_dias = float(input("informe quantos dias o carro esteve alugado: "))
preco_total_dias = quant_dias*60
preco_total_km = quant_km*0.15
var_total = preco_total_dias + preco_total_km
print("o valor total a pagar é "+str(var_total))
