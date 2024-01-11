#Taller Strings
#Sebastian Albarracin Silva y Juan Sebastian Velasquez

def main():
    nombre = input("Ingrese su nombre completo")

    #punto1 mirar cuantas letras tiene el nombre
    cantidadletras = len(nombre)
    cantidadespacios = nombre.count(" ")
    print("El nomber tiene esta cantidad de letras:",cantidadletras - cantidadespacios)

    #punto2 mirar cuantas vocales tiene el nombre
    vocales = "aeiouAEIOU"
    cantvocales = sum([1 for letra in nombre if letra in vocales])
    print("El nombre tiene",cantvocales,"vocales")


    #punto3 cuantas veces aparece una vocal
    vocal = input("¿Que vocal desea buscar en el nombre?")
    cantidad = nombre.lower().count(vocal.lower())
    print("La vocal aparece",cantidad,"veces")
    
    #punto4 convierte todo el nombre a minúsculas
    print("El nombre en minúsculas es:",nombre.lower())

    #punto5 convierte todo el nombre a mayúsculas
    print("El nombre en minúsculas es:",nombre.upper())
    
    #punto6 separa los apellidos y nombres en una lista
    print("Lista de nombres",nombre.split())

    #punto7 convierte la primera letra del nombre en mayúscula
    convertirprimera = [nombre.capitalize() for nombre in nombre.split()]
    for i in range(len(convertirprimera)):
        print (convertirprimera[i],end=" ")
    
    #punto8 dice cuantas cadenas tiene el nombre
    print()
    print("Su nombre tiene",len(nombre.split()),"cadenas")

    #punto9 entrega las posiciones en las que se encuentra una letra dada
    pos = []
    for i in range(len(nombre)):
        if nombre.lower()[i] == vocal:
            pos.append(i)
    print("Su letra se encuentra en las siguientes posiciones",pos)

    #punto10 manda opciones de diminutivo para el nombre
    x = nombre.split()[0]
    if x.endswith("a"):
        print("La primera opción de diminutivo es:",x.lower()[:-1] + "ita")
        print("La segunda opción de diminutivo es:",x.lower()[:-1] + "sita")
    else:
        print("La primera opción de diminutivo es:",x.lower() + "ito")
        print("La segunda opción de diminutivo es:",x.lower() + "sito")
    #punto11 hallar la menor letra del nombre
    print("La letra con el menor valor es:",min(nombre.replace(" ","")))

    #punto12 hallar la mayor letra del nombre
    print("La letra con el mayor valor es:",max(nombre))

    #punto13 armar una dirección de correo electrónico
    correo = "@mail.escuelaing.edu.co"
    sumador = ""
    for i in range(0,len(nombre.split()),2):
        if i == 0:
            sumador = sumador + nombre.lower().split()[i]
        else:
            sumador = sumador + "." + nombre.lower().split()[i]
    print("Su correo quedaría de la siguiente forma:",sumador + correo)
    
main()
