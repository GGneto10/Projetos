#Código direcionado a ajudar pessoas com diferentes rendas a organizar o próprio dinheiro de forma rasa.
#ControleFinanceiro
print('Aqui vamos te ajudar com controle financeiro ' \
'com um suporte Básico de como usar suas economias  ' \
'mas para isso, preciso que me diga')
print('Seu tipo de Controle será [1], [2] ,[3]? \n'
'1 = 60/30/10, 2 = 50/30/20, 3 = 80/10/10')

EscolhadeControle = input('[1], [2], [3]: ')
EntradaSalario = input('E o seu salário, para ajudarmos com valores mais palpavéis: ')

def DescontoINSS(SalarioBruto):
    SalarioBrutoFloat = float(SalarioBruto)

    if SalarioBrutoFloat <= 1518.:
        Desconto1 = (SalarioBrutoFloat * (7.5)) /100
        ResDesconto1 = SalarioBrutoFloat - Desconto1
        return ResDesconto1
    elif 1518.01 >= SalarioBrutoFloat <= 2793.88
        Desconto2 = (SalarioBrutoFloat * (9)) /100
        ResDesconto2 = SalarioBrutoFloat - Desconto2
        return ResDesconto2
    elif 2793.89 >= SalarioBrutoFloat < 4190.83:
        Desconto3 = (SalarioBrutoFloat * (12)) /100
        ResDesconto3 = SalarioBrutoFloat - Desconto3
        return ResDesconto3
    elif SalarioBrutoFloat >= 4190.84:
        Desconto4 = (SalarioBrutoFloat * (14)) /100
        ResDesconto4 = SalarioBrutoFloat - Desconto4
        return ResDesconto4
    ## ## ## ## ## ## ## ## ## ## ## ## ## ##

SalarioDescontadoINSS = DescontoINSS(EntradaSalario) #Oque será chamado 
print(f'Seu salário Descontado do INSS fica: {SalarioDescontadoINSS:.2f}')
#Primeira Parte: Receber o salário e mostrar quanto ele fica Liquido OKAY
#Segunda Parte, onde as Escolhas se envolvem: Andamento
def EscolhadeControle1(SalarioDescontado):
    SalarioDescontadoFloat = float(SalarioDescontado)

    parte60 = ((SalarioDescontadoFloat * 60)/ 100)
    parte30 = ((SalarioDescontadoFloat * 30 )/100)
    parte10 = ((SalarioDescontadoFloat * 10)/ 100)

    PartesEscolha1 =  parte60, parte30, parte10
    return PartesEscolha1
    

def EscolhadeControle2(SalarioDescontado):
    SalarioDescontadoFloat = float(SalarioDescontado)

    parte50 = ((SalarioDescontadoFloat * 50)/ 100)
    parte30 = ((SalarioDescontadoFloat * 30 )/100)
    parte20 = ((SalarioDescontadoFloat * 20)/ 100)

    PartesEscolha2 = parte50, parte30, parte20
    return PartesEscolha2
    

def EscolhadeControle3(SalarioDescontado):
    SalarioDescontadoFloat = float(SalarioDescontado)

    parte80 = ((SalarioDescontadoFloat * 80)/ 100)
    parte10 = ((SalarioDescontadoFloat * 10 )/100)  

    PartesEscolha3 = parte80, parte10, parte10
    return PartesEscolha3
    
if EscolhadeControle == '1':
    Valores1 = (EscolhadeControle1(SalarioDescontadoINSS))
    print(f'Separando seu salário(Já descontado do INSS) fica para: Contas: {Valores1[0]:.2f}R$ , Investimentos: {Valores1[1]:.2f} R$ e Lazer: {Valores1[2]:.2f} R$')

elif EscolhadeControle == '2':
    Valores2 = (EscolhadeControle2(SalarioDescontadoINSS))
    print(f'Separando seu salário(Já descontado do INSS) fica para: Contas: {Valores2[0]:.2f} R$ , Investimentos: {Valores2[1]:.2f} R$ e Lazer: {Valores2[2]:.2f} R$')

elif EscolhadeControle == '3':
    Valores3 = EscolhadeControle3(SalarioDescontadoINSS)
    print(f'Separando seu salário(Já descontado do INSS) fica para: Contas: {Valores3[0]:.2f} R$ , Investimentos: {Valores3[1]:.2f} R$ e Lazer: {Valores3[2]:.2f} R$')

else:
    print('Por favor, esclha uma Opção Válida')

    #Para melhorar esse código: Fazer os valores retornados se separarem (FEITO)