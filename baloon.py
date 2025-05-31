import random
import time
import msvcrt  # Para detectar pressionamento de tecla sem bloquear

def get_input(timeout=0.1):
    """Tenta ler input do usuário sem bloquear a execução"""
    start_time = time.time()
    while True:
        if msvcrt.kbhit():
            return msvcrt.getch().decode()
        if (time.time() - start_time) > timeout:
            return None

def jogar_rodada(aposta):
    """Executa uma rodada completa do jogo"""
    print("\n=== NOVA RODADA ===")
    print("Pressione ESPAÇO para parar e garantir seu multiplicador!")
    print("Se esperar demais, pode explodir e perder tudo!\n")
    
    multiplicador = 1.0
    incremento = 0.1  # Quanto o multiplicador aumenta por segundo
    tempo_explosao = random.randint(5, 30)  # Tempo máximo antes de explodir
    
    print(f"Tempo até possível explosão: {tempo_explosao}s (secreto)")
    print("\nMultiplicador atual: 1.00x")
    
    start_time = time.time()
    
    try:
        while True:
            # Verifica se o jogador quer parar
            key = get_input()
            if key == ' ':
                ganho = aposta * multiplicador
                print(f"\nVocê parou com {multiplicador:.2f}x! Ganhou R${ganho:.2f}")
                return ganho
            
            # Atualiza o multiplicador
            tempo_decorrido = time.time() - start_time
            multiplicador = 1.0 + (tempo_decorrido * incremento)
            
            # Verifica se explodiu
            if tempo_decorrido >= tempo_explosao:
                print(f"\n💥 BOOM! O multiplicador explodiu após {tempo_explosao}s!")
                return 0
            
            # Mostra o multiplicador atual
            print(f"Multiplicador atual: {multiplicador:.2f}x", end="\r")
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nJogo interrompido!")
        return 0

def main():
    """Função principal do jogo"""
    saldo = 1000.00  # Saldo inicial
    
    print("=== JOGO DO MULTIPLICADOR ===")
    print("Regras:")
    print("- Multiplicador começa em 1.0x e aumenta com o tempo")
    print("- Pressione ESPAÇO para parar e garantir seu ganho")
    print("- Se esperar demais, pode explodir e perder tudo!")
    
    while True:
        print(f"\nSaldo atual: R${saldo:.2f}")
        entrada = input("Deseja jogar? [sim/não] ").lower()
        
        if entrada == 'não':
            print("\nObrigado por jogar! Saldo final: R${saldo:.2f}")
            break
            
        if entrada != 'sim':
            print("Opção inválida. Digite 'sim' ou 'não'.")
            continue
            
        try:
            aposta = float(input("Valor da aposta: R$"))
            if aposta <= 0:
                print("Valor deve ser positivo!")
                continue
            if aposta > saldo:
                print("Saldo insuficiente!")
                continue
        except ValueError:
            print("Valor inválido!")
            continue
            
        saldo -= aposta
        ganho = jogar_rodada(aposta)
        saldo += ganho
        
        if saldo <= 0:
            print("\nSeu saldo acabou! Fim de jogo.")
            break

if __name__ == "__main__":
    main()