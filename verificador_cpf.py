
#Recebe o CPF
CPF_cliente = input('Coloque aqui seu CPF(appenas Numerais): ')  #74682489070
if not CPF_cliente.isdigit():
    print('Apenas Numeros, por favor.')     #Confere se são apenas números, se não for, quebra o código

nove_digitos = CPF_cliente[:9] #Corta até o nono número

cont_1 = 10     #Contador
res_digito1 = 0 #Variável de armazenar o resultado

for digito in nove_digitos:     #para cada digito nos nove digitos que eu quero

    res_digito1 += int(digito) * cont_1     # Pego o res e atribuo que o numeral digito sera multiplicado pelo seu número do contador
    cont_1 -= 1     #Diminui o contador em 1

digito_1 = ((res_digito1 * 10) % 11)    #Multiplico o resultado por 10 e faço o resto da divisão por 11 para verificar se está correto
digito_1 = digito_1 if digito_1 <= 9  else 0
 ###############################################
dez_digitos = nove_digitos + str(digito_1) 

cont_2 = 11     #Contador
res_digito2 = 0 #Variável de armazenar o resultado

for digito in dez_digitos:
    res_digito2 += (int(digito) * cont_2)
    cont_2 -= 1 
digito_2 = (res_digito2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0


Cpf_peloCalc = f'{nove_digitos}{digito_1}{digito_2}'
print(Cpf_peloCalc)

if CPF_cliente == Cpf_peloCalc:
    print('CPF válido')
else:
    print('CPF inválido')
