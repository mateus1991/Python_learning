print ("Sendo a equação: ax^2+bx+c\n") #second grade equation
a = float(input("digite o valor de a:"))
b = float(input("digite o valor de b:"))
c = float(input("digite o valor de c:"))

delta =  (b*b) - (4*a*c)

if delta < 0:
    print ("A equação não possui raizes reais") #non-real roots
else:
    raiz1 = ((b*-1)+(delta**0.5))/(2*a)
    raiz2 = ((b*-1)-(delta**0.5))/(2*a)
    print ("As raizes são: "+ str(raiz1) +" e "+ str(raiz2)) #roots