import matplotlib.pyplot as plt

dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))  # First cell has the year
        y.append(int(linha[1]))  # Second cell has the population


plt.title("Crescimento da população brasileira")
plt.xlabel("Ano")
plt.ylabel("População")
plt.bar(x,y, color="#e4e4e4", linestyle="--")
plt.plot(x,y)

plt.show()