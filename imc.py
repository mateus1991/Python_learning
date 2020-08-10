# Calculadora de IMC

def imcCalc (peso,altura):
    try:
        imc = (peso/(altura*altura))
    
        if imc < 16:
            return ("Seu IMC é "+str(imc)+" - Magreza severa")
        elif imc < 17:
            return ("Seu IMC é "+str(imc)+" - Magreza moderada")
        elif imc < 18.5:
            return ("Seu IMC é "+str(imc)+" - Magreza leve")
        elif imc < 25:
            return ("Seu IMC é "+str(imc)+" - Saudável")
        elif imc < 30:
            return ("Seu IMC é "+str(imc)+" - Sobrepeso")
        elif imc < 35:
            return ("Seu IMC é "+str(imc)+" - Obesidade grau I")
        elif imc < 40:
            return ("Seu IMC é "+str(imc)+" - Obesidade grau II (severa)")
        else:
            return ("Seu IMC é "+str(imc)+" - Obesidade grau III (mórbida)")

    except:
        return print ("Numero inválido")


peso = float(input("Entre com seu peso:"))
altura = float(input("Entre com sua altura:"))

print (imcCalc(peso,altura))
