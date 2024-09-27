var_pay = int(input("informe seu salário por hora: "))
var_day = int(input("informe o total de dias trabalhados: "))
var_hour = int(input("informe o total de horas trabalhadas por dia: "))
var_total_hour = var_day*var_hour
var_total_pay = var_total_hour*var_pay
print ("O total de horas trabalhadas é de "+ str(var_total_hour))
print ("Seu salário no fim do mês será de "+ str(var_total_pay))
