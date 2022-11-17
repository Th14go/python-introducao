minha_string = "Thiago Henrique Lopes"

#Quebra a lista inserindo espaço entre as strings#
minha_lista = minha_string.split(" ")
print(minha_lista)

#Busca uma string e retorna em qual posição se encontra a string#
busca = minha_string.find("Lo")
print(busca)

#Substitui string com o replace#
minha_string = minha_string.replace ("Henrique", " ")
print (minha_string)

#Remove Espaços inicial e final com o strip#
removeespaco = " Thiago Lopes "
print (removeespaco.strip())
