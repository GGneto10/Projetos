#Esse código recebe um gabarito, do professor, e usa ele de 
#Base para respostas de prova

relacao = {}
gabarito = input('Olá professor(a), insira por favor as respostas do gabarito: ').split() 

while True:

    nome_do_aluno = input("Digite o nome do aluno (ou 'sair' para terminar): ")
    if nome_do_aluno.lower() == 'sair':
        break
    respostas = input("Digite as respostas do aluno separadas como no exemplo (ex: C A B C): ").split()
    relacao[nome_do_aluno] = respostas

    if len(respostas) != len(gabarito):
        print(f"AVISO: {nome_do_aluno} tem {len(respostas)} respostas (o gabarito tem {len(gabarito)}). A nota será 0.")
        relacao[nome_do_aluno] = {'respostas': respostas, 'nota': 0}
        continue

print("\n--- RESULTADOS ---")
print(f"Gabarito oficial: {' '.join(gabarito)}\n")

for nome, respostas in relacao.items():
    nota = 0
    # Verifica se o aluno tem o mesmo número de questões que o gabarito
    if len(respostas) == len(gabarito):
        nota = sum(1 for i in range(len(gabarito)) if respostas[i] == gabarito[i])
    else:
        print('O aluno não colocou em seu gabarito a quantidade necessária de questões para ser verificado.')
        nota = 0  # Se não, nota = 0
    
    # Exibe o resultado formatado
    print(f"{nome} - Respostas: {' '.join(respostas)} | Nota: {nota}/{len(gabarito)}")

