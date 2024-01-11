import random
m = int(input("¿Cuántos valores aleatorios desea generar?"))
n = int(input("Ingrese el rango en el que desea generar los números al azar"))
lista = []
for i in range (0,n):
    lista.append(i)

for i in range(0,n):
    pos = random.randint(0,i)    
    aux = lista[i]
    lista[i] = lista[pos]
    lista[pos] = aux
    pedazo = lista[0:6]

print("Los números aleatorios generados són",pedazo)





