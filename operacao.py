def Operacao (num1, num2):
    if op == "+":          #Addition
        return num1+num2
    elif op == "-":        #Subtraction
        return num1-num2
    elif op == "*":        #Multiplication
        return num1*num2
    elif op == "/":        #Division
        try:               #Avoiding division by 0
            return num1/num2
        except:
            print ("Décimo primeiro mandamento: Não dividirás por 0") 
            return False
    else:
        print ("Nenhuma opção válida foi escolhida") #Not valid option
        return False



num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))

op = input ("Operação:\n+ para adição\n- para subtração\n* para multiplicação\n/ para divisão\nQual a sua escolha:")

result = Operacao (num1,num2)

if result != False:
    print ("O resultado da operação é: "+str(result))