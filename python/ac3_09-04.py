# Caso seja resolvido em duplas, coloque os nomes da dupla aqui:
# Nome1: 
# Nome2:

# Este exercício é sobre o uso da estrutura de seleção (if/elif/else),
# portanto NÃO é para ser usado nenhum comando de laço de repetição (while).

# Não coloque nenhum texto para pedir o dado de entrada para o usuário.

# Imprima exatamente a frase: "Desconto do INSS: R$ <valor>", sem as aspas.
# Substituíndo <valor> pelo valor calculado e com duas casas decimais.
inss= 0
salario = float(input(""))

if salario <= 1751.81:
  inss = salario*(8/100)
elif salario >= 1751.82 and salario <= 2919.72:
  inss = salario*(9/100)
elif salario >= 2919.73 and salario <= 5839.45:
  inss = salario*(11/100)
elif salario > 5839.45:
  inss = 5839.45*(11/100)
print("Desconto do INSS: R$ {:.2f}".format(inss))