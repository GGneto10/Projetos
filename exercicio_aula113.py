#Exerciciozinho

def multiplica(*args):
    total = 1
    for number in args:
        total *= number
    return total

def par_impar(number):
    if number % 2 == 0:
        return f'{number} é par'
    else:
        return f'{number} é ímpar'



value = multiplica(3)
mostrar = par_impar(value)

print(value)
print(mostrar)




