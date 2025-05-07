import os


lista = []
while True:
    print('Selecione uma opção')
    option = input("[I]inserir, [A]apagar, [L]listar: ").upper()

    if option == 'I':

        os.system('cls')
        value = input('Item a ser listado: ')
        lista.append(value)

    elif option == 'A':
        indice_str = input('Qual indice da lista gostaria de apagar: ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite um número do Índice que deseja apagar.')
        except IndexError:
            print('Este índice não existe na lista.')


    elif option == 'L':

        os.system('cls')
        
        if len(lista) == 0:
            print('Não há nada para listar')

        for i, value in enumerate(lista):
            print(value)    
    else:
        print('Por favor, selecione uma das opções.')        
