#Trabajo sumatoria de cuadrados
#Juan Seastián Velásquez Rodríguez

numero = int(input("Bienvenido,digite el número hasta el que desea sumar los cuadrados"))
contador = 0
sumador = 0

while contador <= numero:
    resultado = contador * contador
    sumador = sumador + resultado
    contador = contador + 1

print("Este es el resultado",sumador)
