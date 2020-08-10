import random

def gera_voto ():

    votos = []

    for i in range(15):
        votos.append(random.randint(1,5))

    return votos

def contagem (votos,opcao):

    if opcao == 1:
        candidadoA = votos.count(1)
        return candidadoA
    elif opcao == 2:
        candidadoB = votos.count(2)
        return candidadoB
    elif opcao == 3:
        candidadoC = votos.count(3)
        return candidadoC
    elif opcao == 4:
        nulo = votos.count(4)
        return nulo
    elif opcao == 5:
        branco = votos.count(5)
        return branco
    else:
        return "Opção inválida"

votos = gera_voto()

print ("O candidato A recebeu "+str(contagem(votos,1))+" votos")
print ("O candidato B recebeu "+str(contagem(votos,2))+" votos")
print ("O candidato C recebeu "+str(contagem(votos,3))+" votos")
print (str(contagem(votos,4))+" votos foram nulos")
print (str(contagem(votos,5))+" votos foram em branco")

nulo_per = ((contagem(votos,4))/15)*100
branco_per = ((contagem(votos,5))/15)*100

print ("A porcentagem de votos nulos foi de "+ str(nulo_per)+"%")
print ("A porcentagem de votos brancos foi de "+ str(branco_per)+"%")
