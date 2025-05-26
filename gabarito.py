#Esse código recebe um gabarito, do professor, e usa ele de 
#Base para respostas de prova
nota = 0
respostas_do_gabarito = input('Olá, professor, insira por favor as respostas do gabarito: ').split() 
respostas_do_aluno = input('Aqui sera o gabarito do aluno: ').split() 

if len(respostas_do_aluno) == len(respostas_do_gabarito):  #Verifico se a quantidade de Respostas do aluno é igual a quantidade de respostas do gabarito
    if respostas_do_gabarito == respostas_do_aluno:
        print('4/4')
    else:
        Oque_esta_certo = [0,1,2,3]
        for i in Oque_esta_certo:
            questões_acertadas = respostas_do_gabarito[i] == respostas_do_aluno[i]
            if questões_acertadas:
                print(f'A questão {i} na {respostas_do_aluno[i]} está correta.')
                nota += 1
            else:
                print(f'A questão {i} do aluno segundo o {respostas_do_gabarito} está errada.')
            

    print(f"Gabarito: {respostas_do_gabarito}")
    print(f'Aluno: {respostas_do_aluno}')
    print(f'A nota é: {nota}/4')

elif len(respostas_do_aluno) >= len(respostas_do_gabarito):
    print('Prova zerada. 0/0')
else: 
    print('Prova zerada. 0/0')

#Para melhorar esse código: Criar uma lista de alunos, e cada resposta deles deve ser exibida com seu nome ao final em uma lista
#para aprimorar: Sistema de notas, adcionar notas de acordo com a quantidade de acertos.