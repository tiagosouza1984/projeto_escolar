#Nomes caso feito em duplas:
#Nome1:Tiago da Silva Souza
#Nome2:Brenda Macedo de Oliveira
flag = False

while not flag:
  var_entry = input("")
  if var_entry =="Próximo":
    print("Aguardando dados do próximo pacote!")
  if var_entry =="Sair":
      print("Programa encerrado!")
      flag = True
  if var_entry !="Próximo" and var_entry !="Sair":
      print("Comando não reconhecido, digite novamente!")
    

