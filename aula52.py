''' 
aula92
Números flutuantes podem ser imprecisos em sua soma
'''
import decimal
#modulo decimal, assistir a aula 92 se for preciso.

n1 = 0.1
n2 = 0.2
n3 = n1 + n2
print(n3)
print(f'{n3:.2f}')
print(round(n3, 2))
#exemplo prático, e função ROUND

