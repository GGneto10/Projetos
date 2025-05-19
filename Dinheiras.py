#Código direcionado a ajudar pessoas com diferentes rendas a organizar o próprio dinheiro de forma rasa.
#ControleFinanceiro
print('Aqui vamos te ajudar com controle financeiro ' \
'com um suporte Básico de como usar suas economias  ' \
'mas para isso, preciso que me diga')
print('Seu tipo de Controle será [1], [2] ,[3]? \n'
'1 = 60/30/10, 2 = 50/30/20, 3 = 80/10/10')

Escolha_de_Controle = input('[1], [2], [3]: ')
Entrada_Salario = input('E o seu salário, para ajudarmos com valores mais palpáveis: ')

def Desconto_INSS(Salario_Bruto):
    try:
        Salario_Bruto_Float = float(Salario_Bruto)

        if Salario_Bruto_Float <= 1518.00:
            Desconto = Salario_Bruto_Float * 0.075
        elif 1518.01 <= Salario_Bruto_Float <= 2793.88:
            Desconto = Salario_Bruto_Float * 0.09
        elif 2793.89 <= Salario_Bruto_Float <= 4190.83:
            Desconto = Salario_Bruto_Float * 0.12
        else:
            Desconto = Salario_Bruto_Float * 0.14
        
        return Salario_Bruto_Float - Desconto
    except ValueError:
        print("Por favor, insira um valor numérico válido para o salário.")
        return None

Salario_Descontado_INSS = Desconto_INSS(Entrada_Salario)

if Salario_Descontado_INSS is not None:
    print(f'Seu salário descontado do INSS fica: {Salario_Descontado_INSS:.2f} R$')

    def Escolha_de_Controle_1(Salario_Descontado):
        Salario_Descontado_Float = float(Salario_Descontado)
        parte60 = Salario_Descontado_Float * 0.60
        parte30 = Salario_Descontado_Float * 0.30
        parte10 = Salario_Descontado_Float * 0.10
        return parte60, parte30, parte10

    def Escolha_de_Controle_2(Salario_Descontado):
        Salario_Descontado_Float = float(Salario_Descontado)
        parte50 = Salario_Descontado_Float * 0.50
        parte30 = Salario_Descontado_Float * 0.30
        parte20 = Salario_Descontado_Float * 0.20
        return parte50, parte30, parte20

    def Escolha_de_Controle_3(Salario_Descontado):
        Salario_Descontado_Float = float(Salario_Descontado)
        parte80 = Salario_Descontado_Float * 0.80
        parte10 = Salario_Descontado_Float * 0.10
        return parte80, parte10, parte10

    if Escolha_de_Controle == '1':
        Valores = Escolha_de_Controle_1(Salario_Descontado_INSS)
        print(f'Separando seu salário (já descontado do INSS) fica para:')
        print(f'Contas: {Valores[0]:.2f} R$')
        print(f'Investimentos: {Valores[1]:.2f} R$')
        print(f'Lazer: {Valores[2]:.2f} R$')

    elif Escolha_de_Controle == '2':
        Valores = Escolha_de_Controle_2(Salario_Descontado_INSS)
        print(f'Separando seu salário (já descontado do INSS) fica para:')
        print(f'Contas: {Valores[0]:.2f} R$')
        print(f'Investimentos: {Valores[1]:.2f} R$')
        print(f'Lazer: {Valores[2]:.2f} R$')

    elif Escolha_de_Controle == '3':
        Valores = Escolha_de_Controle_3(Salario_Descontado_INSS)
        print(f'Separando seu salário (já descontado do INSS) fica para:')
        print(f'Contas: {Valores[0]:.2f} R$')
        print(f'Investimentos: {Valores[1]:.2f} R$')
        print(f'Lazer: {Valores[2]:.2f} R$')

    else:
        print('Por favor, escolha uma opção válida (1, 2 ou 3).')