import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,7,3,0]

titulo = "Grafico de Barras"
eixox = "Eixo X"
eixoy = "Eixo Y"
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.bar(x,y)
plt.show()

