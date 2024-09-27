#Nomes caso feito em duplas:
#Nome1:
#Nome2:
flag = False
var_entry = input("")

while not flag:
    if var_entry =="Próximo":
        print("Aguardando dados do próximo pacote!")
        flag = True
    if var_entry =="Sair":
        print("Programa encerrado!")
        flag = True
    if var_entry !="Próximo" and var_entry !="Sair":
        print("Comando não reconhecido, digite novamente!")
        var_entry = input("")
    

