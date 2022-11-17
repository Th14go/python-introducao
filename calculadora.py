#
num1 = int(input ("Digite o primeiro número: "))
operador = input ("Digite o operador: ")
num2 = int(input ("Digite o segundo número: "))


if operador == "+":
     resultado = num1 + num2

elif operador == "-":
    resultado = num1 - num2

elif operador == "/":
    resultado = num1 / num2

elif operador == "*":
    resultado = num1 * num2

print (resultado)