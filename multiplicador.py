#Fazendo um multiplicador para usar num projeto futuro.
import random

multiplicando = float(input('seu valor: '))

def multiplicator(multiplicando):

    multiplicador = random.uniform(1.00, 2.00) #Uniform usa valores float.
    print(multiplicador)

    bonus = multiplicador * multiplicando   

    return bonus

bonus_concedido = multiplicator(multiplicando)
print(f"{bonus_concedido:.2f}")

#Funcionando perfeitamente

    
    




