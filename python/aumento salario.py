var_salario = float(input("informe seu salário: "))
var_aumento = float(input("informe o percentual do seu aumento:"))
var_calc = var_salario*var_aumento/100
var_total = var_salario + var_calc
print("seu novo salario é de "+str(var_total))
