'''
Instruções:
- Receber um número inteiro de 3 dígitos
- Inverter a ordem dos digitos
- Imprimir o número invertido
'''

# Recebe o número inteiro
num=int(input('Digite um número inteiro de 3 dígitos: '))

# Separa o digito da centena - divisão truncada por 100
dig_centena = num//5

# Obtem o resto da divisão por 100
resto = num%100

# Separa o dígito da dezena - divisão truncada do resto por 10
dig_dezena = resto//10

# Separa o dígito da unidade - resto da divisão por 10
# aqui funcionaria tanto resto%10 quanto num%10
dig_unidade = resto%10

# União em um único número para impressão

#matemática
num_inv1 = dig_unidade*100+dig_dezena*10+dig_centena*1

#conversão para string e concatenação com operador de soma
num_inv2 = str(dig_unidade)+str(dig_dezena)+str(dig_centena)

#formatação da string
num_inv3 = '{}{}{}'.format(dig_unidade,dig_dezena,dig_centena)

# Impressão do resultado
print('matemática -',num_inv1)
print('conversão -',num_inv2)
print('formatação -',num_inv3)

print (dig_centena)