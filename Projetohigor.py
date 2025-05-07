glicemiaINPUT = input("Qual sua glicemia atual: ")
glicemia = int(glicemiaINPUT)

def check(Glicose):
    if Glicose <= 99:
        print('está tudo bem')

    if Glicose > 99:
        print('Opa, calma sua glicose está acima de 99mg/hg ')

    if Glicose >= 125:
        print('Procure seus remédios e controle-se')

    

print(check(glicemia))






    
