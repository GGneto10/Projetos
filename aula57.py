salas = [ 
    ['Maria', 'Helena' ,],#0

    ['Elaine', ],#1

    ['Luiz', 'João', 'Eduarda', (0, 22, 44, 55) ]#2

    ]
'''
print(salas[2][2]) #Puxo a lista de indice 2, e o indice 2 dela
 #Como funciona lista de listas e seus indices

print(salas[2][3][1]) #Lista de indice 2, indice 3 da lista
#e o indice 1 da tupla, um pouco confuso, mas compreensivel.
'''

for sala in salas: #cada sala, nas SALAS (lista)
    for item in sala: #cada ITEM na SALA -  mostra apenas o item
        print(item)
 