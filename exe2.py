# -*- coding: utf-8 -*-
nota1 = float (input("Digita a sua nota 1:"))
nota2 = float (input("Digite sua nota 2:"))

media = (nota1 + nota2) /2

print

if media >=6:
    print("Aprovado: " +str(media))
else:
    print ("Reprovado: " +str(media))
