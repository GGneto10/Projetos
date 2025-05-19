import os
import random

numero_para_adivinhar = random.randint(1, 100)
print(numero_para_adivinhar)
chances = 10
while chances >= 0 :
    
    print("Adivinhe o número \n"
    ' Você deve colocar dois números diferentes de 0 a 100, e a soma deles deve dar um numero especifíco,' \
    'quando acertar aparecerá: "Zerou" ')    
    try:
        print(f'Você tem mais {chances} chances para acertar o número.')
        x = int(input('X:'))
        y = int(input('Y:'))
        os.system('cls')

        Somatorio = x + y

        if Somatorio == numero_para_adivinhar:
            print('Zerou')
            print(f'{chances} chances sobraram')
            if chances <= 0:
                break
            break

        elif Somatorio < numero_para_adivinhar:
            print(f'"{Somatorio}" é número errado, o número é maior.')
            chances -= 1
            
            continue
        elif Somatorio > numero_para_adivinhar:
            print(f'"{Somatorio}" é número errado, o número é menor.')
            chances -= 1
            continue 


    except ValueError:
        print('Por favor, um número Inteiro')
        chances -= 1
        os.system('cls')

        continue

