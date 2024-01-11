#Cambio de base 10 a base 2
#Juan Sebastian Velasquez Rodriguez

numero = int(input("Bienvenido, ingrese el número en base 10 que desea cambiar a base 2 (binario)"))

if numero % 2 == 0:
    resultado = ""

if numero % 2 == 1:
    resultado = ""

if numero == 0:
    resultado = "0"

while numero >= 1:
    mod = numero % 2
    numero = numero // 2
    if mod == 0:
        resultado = "0" + resultado 
    if mod == 1:
        resultado = "1" + resultado

print("Este es su nuevo número en binario:",resultado)



