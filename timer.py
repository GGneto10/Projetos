import time

def contador_regressivo(minutos):
    segundos = minutos * 60
    while segundos > 0:
        mins, segs = divmod(segundos, 60)
        tempo_formatado = f"{mins:02d}:{segs:02d}"
        print(tempo_formatado, end="\r")
        time.sleep(1)
        segundos -= 1

contador_regressivo(1)  # Contagem de 10 minutos
# contador_regressivo(5) 