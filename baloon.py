import time
import math
import msvcrt
import sys

def get_input():
    """Verifica se uma tecla foi pressionada"""
    if msvcrt.kbhit():
        return msvcrt.getch().decode()
    return None

def jogar_rodada(aposta):
    """Executa uma rodada com multiplicador acelerado"""
    print("\n=== NOVA RODADA ===")
    print("Pressione ESPAÇO para parar e garantir seu multiplicador!")
    print("Quanto mais esperar, mais rápido o multiplicador sobe, mas cuidado com a explosão!\n")
    
    multiplicador = 1.0
    tempo_explosao = random.randint(0, 12)  # Tempo até possível explosão
    tempo_inicio = time.time()
    base_speed = 0.1  # Velocidade inicial
    acceleration = 0.05  # Aceleração por segundo
    
    print(f"Tempo até possível explosão: {tempo_explosao}s (secreto)")
    
    try:
        while True:
            tempo_decorrido = time.time() - tempo_inicio
            
            # Cálculo do multiplicador com aceleração (função quadrática)
            speed = base_speed + (acceleration * tempo_decorrido)
            multiplicador = 1.0 + (speed * tempo_decorrido)
            
            # Verifica se o jogador quer parar
            key = get_input()
            if key == ' ':
                ganho = aposta * multiplicador
                print(f"\nVocê parou com {multiplicador:.2f}x! Ganhou R${ganho:.2f}")
                return ganho
            
            # Verifica se explodiu
            if tempo_decorrido >= tempo_explosao:
                print(f"\n💥 BOOM! Explodiu após {tempo_explosao:.1f}s com multiplicador em {multiplicador:.2f}x!")
                return 0
            
            # Mostra informações em tempo real
            sys.stdout.write(f"\rTempo: {tempo_decorrido:.1f}s | Multiplicador: {multiplicador:.2f}x | Velocidade: {speed:.3f}/s")
            sys.stdout.flush()
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\nJogo interrompido!")
        return 0

def main():
    """Função principal do jogo"""
    saldo = 1000.00
    
    print("=== JOGO DO MULTIPLICADOR ACELERADO ===")
    print("Regras:")
    print("- Multiplicador começa em 1.0x e acelera com o tempo")
    print("- Pressione ESPAÇO para parar e garantir seu ganho")
    print("- Se esperar demais, explode e você perde tudo!")
    
    while saldo > 0:
        print(f"\nSaldo atual: R${saldo:.2f}")
        entrada = input("Jogar? [sim/não] ").lower()
        
        if entrada == 'não':
            print(f"\nSaldo final: R${saldo:.2f}")
            break
            
        if entrada != 'sim':
            continue
            
        try:
            aposta = float(input("Aposta: R$"))
            if aposta <= 0 or aposta > saldo:
                print("Valor inválido!")
                continue
        except:
            print("Digite um número válido!")
            continue
            
        saldo -= aposta
        ganho = jogar_rodada(aposta)
        saldo += ganho
    
    if saldo <= 0:
        print("\nFALIDO! Saldo zerado.")

if __name__ == "__main__":
    import random
    main()