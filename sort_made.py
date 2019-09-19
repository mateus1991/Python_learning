# Selection sort algorithm

lista = [9,7,1]

for i in range(len(lista)):

    menor = i

    for j in range(i+1,len(lista)):
        if lista [j] < lista [menor]:
            menor = j                  #findind minor by step

    if lista[i] != lista[menor]:
        aux = lista[i]
        lista[i] = lista[menor] #changing psitions on list
        lista [menor] = aux

print (lista)