import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [2,3,7,1,0]
z = [100,200,300,900]


titulo = "Grafico de Barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.plot(x,y, color="#009900", linestyle="-")
plt.scatter(x,y, label="Meus pontos", marker=".", s=z )
plt.legend
plt.show()

#salva grafico como imagem
plt.savefig("figura.png", dpi=300)
