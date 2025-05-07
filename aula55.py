'''
split e join com list e str
split - divide uma str
join - une uma str
'''

frase = "XQDL DA SILVA JUNIOR"
lista_palavras = frase.split(' ')

for i, frases in enumerate(lista_palavras):
    print(lista_palavras[i].strip())
#strip == corta os espaços

vaitomarnocuAZULE = "-".join('Vai se fuder azule')
print(vaitomarnocuAZULE)