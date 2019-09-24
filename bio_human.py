entrada = open("human.fasta").read()
saida  = open("human.html","w")

cont = {}
entrada = entrada.replace("\n","")

for i in ["A","T","C","G"]:
    for j in ["A","T","C","G"]:
        cont[i+j]=0



for k in range(len(entrada)-1):
    try:
        cont[entrada[k]+entrada[k+1]] += 1
    except:
        pass

print(cont)

#html
saida.write("<div>")

i = 1
for k in cont:
    transparencia = cont[k]/max(cont.values())   #divide o valor atual pelo maior valor dentro da lista
    saida.write("<div style='width:100px; border:1px solid #111;\n color:#fff; height:100px; float:left; background-color:rgba(0,0,255,"+str(transparencia)+"')>"+k+"</div>")
    if i%4 == 0:
        saida.write("<div style='clear:both'></div>")
    i += 1
 
saida.close()
