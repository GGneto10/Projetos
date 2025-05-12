import random

nove_digitos = '' 
for i in range (9):
    nove_digitos += str(random.randint(0, 9))


cont_1 = 10     
res_digito1 = 0 

for digito in nove_digitos:   

    res_digito1 += int(digito) * cont_1     
    cont_1 -= 1    

digito_1 = ((res_digito1 * 10) % 11)    
digito_1 = digito_1 if digito_1 <= 9  else 0
 ###############################################
dez_digitos = nove_digitos + str(digito_1) 

cont_2 = 11     
res_digito2 = 0 

for digito in dez_digitos:
    res_digito2 += (int(digito) * cont_2)
    cont_2 -= 1 
digito_2 = (res_digito2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0


Cpf_peloCalc = f'{nove_digitos}{digito_1}{digito_2}'
print(f"Primeiros 9 digitos do CPF: {nove_digitos}")
print(f'CPF completo criado: {Cpf_peloCalc}')

