#Apenas um jogo que eu idealizei enquanto tava voltando pra casa, da faculdade.
import random
import time


#Reaproveitar um código

def contador_regressivo(minutos):
    segundos = minutos * 60
    while segundos > 0:
        mins, segs = divmod(segundos, 60)
        tempo_formatado = f"{mins:02d}:{segs:02d}"
        print(tempo_formatado, end="\r")
        time.sleep(1)
        segundos -= 1


quantidade_de_bombas = random.randint(1, 8)
bombas_desarmadas = 0 #talvez eu tire depois

cores_de_fios = ['Verde', 'Vermelho', 'Azul', 'Rosa']   



while True:
    dificuldade = input('Olá, bem vindo ao Bomb Game, Gostaria de jogar no Fácil[F] ou no Dificil[D]?: ')
    if dificuldade.upper() == 'F':
        print(f'Você tem 10 minutos para desarmar {quantidade_de_bombas} de bombas, boa sorte.')
        print(f'{cores_de_fios} são as cores de fios de todas as bombas.') 
        
        while quantidade_de_bombas > 0:
             fio_certo = random.choice(cores_de_fios)
             print(fio_certo)

             escolha = input('Você tem na sua frente uma boa, qual fio vai cortar? ')
             if escolha.lower() == fio_certo.lower():
                quantidade_de_bombas -= 1 
                print(f'{quantidade_de_bombas} ainda faltam.')
             else:
                 print('BOOM!')
                 break
    print('Breakou.')
    break
             

        #contador_regressivo(10)