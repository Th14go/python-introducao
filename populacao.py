#Populacao Brasileira 1980 a 2016
import matplotlib.pyplot as plt

dados = open ("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.bar(x,y)
plt.title("Crescimento População de 1980 a 2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
plt.show()
