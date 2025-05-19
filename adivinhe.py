import os
import random

numero_para_adivinhar = random.randint(1, 100)
print(numero_para_adivinhar)
while True:
    
    print("Adivinhe o número \n"
    ' Você deve colocar dois números diferentes de 0 a 100, e a soma deles deve dar um numero especifíco,' \
    'quando acertar aparecerá: "Zerou" ')    
    try:
        x = int(input('X:'))
        y = int(input('Y:'))
        os.system('cls')

        Somatorio = x + y

        if Somatorio == numero_para_adivinhar:
            print('Zerou')
            break
        
        elif Somatorio < numero_para_adivinhar:
            print(f'"{Somatorio}" é número errado, o número é maior.')
            
            continue
        elif Somatorio > numero_para_adivinhar:
            print(f'"{Somatorio}" é número errado, o número é menor.')
            
            continue
            
        else:
            print('O que caralhos vc acabou de fazer? digite NÚMEROS, N Ú M E R O S, entendeu? Inteiros.')
    except ValueError:
        print('Por favor, um número Inteiro')
        os.system('cls')

        continue

