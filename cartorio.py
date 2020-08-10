# Nomes com iniciados com letra maiuscula

def capitalizacao (nome):

    separado = nome.split()

    for i in range(len(separado)):

        if separado[i] != ("de" and "da"):
            separado[i] = separado[i].capitalize()

    if len(separado) != 1:

        nome = ""

        for i in range(len(separado)):
            nome = nome + separado[i] + " "
    else:

        nome = separado[0]

    return nome
    


nome_input = input("Entre com o nome:")

print ("Nome padronizado é: "+ capitalizacao(nome_input))