
def cutString (frase):
    
    if len(frase) > 15:
        frase = frase[:12]+"..."

    return frase


frase = input("Entre com a frase:")
print ("Frase com max 15 caracteres:\n"+ cutString(frase))
