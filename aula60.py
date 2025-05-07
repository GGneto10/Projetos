'''
Operação ternária (Condição de Apenas uma Linha)
'''

"""condicao = 100 == 100
variavel = 'Valor' if condicao else 'Outro Valor'
print(variavel)"""

digito = 9 # > 9 = 0
#novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

#Da pra bagunçar o codigo se for vários IF numa só linha.