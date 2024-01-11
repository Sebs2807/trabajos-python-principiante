
#Programa saber el numero mayor
#Juan Sebastián Velásquez Rodríguez

def main():
    n = int(input("¿Cuantos valores desea ingresar?"))
    nombre = str(input("Ingrese el nombre del dueño de la edad"))
    edad = int(input("Ingrese edad"))
    mayor = edad
    menor = edad
    contador = 1
    suma = edad
    nombrem = str(nombre)
    nombreM = str(nombre)
    while contador < n:
        contador = contador + 1
        nombre = str(input("Ingrese el nombre del dueño de la edad"))
        edad = int(input("Ingrese edad"))
        if edad >= mayor:
            nombreM = nombre
            mayor = edad
        if edad < mayor:
            mayor = mayor
        if edad <= menor:
            nombrem = nombre
            menor = edad
        if edad > menor:
            menor = menor
        suma = suma + edad
        

    print("La edad mayor es",nombreM, mayor)
    print("La edad menor es",nombrem, menor)
    print("El promedio de edades es",suma / n)

main()
        
    
    
