def convert2celcius (far):

    celsius = (((far-32)/9)*5)

    return celsius


Fahrenheit = float(input("Entre com a temperatura em Fahrenheit: "))
print("Temperatura é: "+str(convert2celcius(Fahrenheit))+"°C")