def isTriangulo (a,b,c):

    if (a <= b+c) and (b <= a+c) and (c <= a+b):
        return "É um triangulo"
    else:
        return "Não é um triangulo"

a = float(input("Entre com o primeiro lado:"))
b = float(input("Entre com o segundo lado:"))
c = float(input("Entre com o terceiro lado:"))

print (isTriangulo(a,b,c))