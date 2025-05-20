#Calculo de IMC, função de IMC
#Exercicio básico, só que em função
Kgs = float(input('Peso em KGs: '))
Centimetros = float(input('Altura em Centimetros: '))

Metros = Centimetros/100 

print(f'Sua altura em metros: {Metros:.2f}')

def IMC(Kg, metros):

    calculo = Kg/(metros*metros)
    print(calculo)

    if calculo < 18.5:
        print(f'seu IMC é {calculo:.1f}, você está Abaixo do Peso ideal.')

    elif calculo >= 18.5 and calculo <= 24.9:
        print(f'seu IMC é {calculo:.1f} você está com o peso ideal.')

    elif calculo >= 25.0 and calculo <= 29.9:
        print(f'seu IMC é {calculo:.1f} você está com Sobrepeso.')

    elif calculo >= 30.0 and calculo <= 34.9:
        print(f'seu IMC é {calculo:.1f} você está com Obesidade grau I.')

    elif calculo >= 35.0 and calculo <= 39.9:
        print(f'seu IMC é {calculo:.1f} você está com Obesidade grau II.')

    elif calculo >= 40.0:
        print(f'seu IMC é {calculo:.1f} você está com Obesidade grau III(mórbida).')

print(IMC(Kgs, Metros))




