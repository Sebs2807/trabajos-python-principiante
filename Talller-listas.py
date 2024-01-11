def valida_dato(lista,long):
    for i in range(long):
        try:
            lista[i] = int(lista[i])
        except ValueError:
            try:
                lista[i] = float(lista[i])
            except ValueError:
                pass
    return lista
def espaciados(lista,long):
    """Imprime los valores de una lista, con espacio entre ellos
    (list,int) -> int
    """
    print("Estos son los valores que conforman a la lista con espacio entre ellos")
    for i in range(long):
        print(lista[i],end=" ")
    print(" ")
def linea1(lista,long):
    """Imprime los valores de la lista, uno en cada linea
    (lista,int) -> int
    """
    print("Estos son los valores que conforman la lista, uno en cada linea")
    for i in range(long):
        print(lista[i])
def elementos(long):
    """Da la cantidad de valores que hay en una lista"""
    print("Esta es la cantidad de valores que hay en la lista:",long)
def pares (lista,long):
    """Retorna la cantidad de pares en una lista de valores enteros
    (list) -> int
    """
    cont = 0
    for i in range(long):
        n = lista[i]
        if n % 2 == 0:
            cont = cont + 1
    return cont
def mitades(lista,long):
    """Retorna una lista tomando solo los valores desde la mitad hasta el final
    (list) -> int
    """
    n = (long // 2)
    pedazo = lista[n:long]
    
    return pedazo
def pos_pares(lista,long):
    """Da los valores que hay en las posiciones pares de un arreglo
    (list) -> list
    """
    afinal = []
    for i in range (long):
        if i % 2 == 0:
            afinal.append(lista[i])
    return afinal
def mitades2(lista,long):
    """Divide un arreglo en 2, el primer arreglo es desde la mitad hacia la izquierda y el otro es desde la mitad + 1 hacia la derecha
    (list) -> list
    """
    n = (long // 2)
    pedazo = lista[0:n + 1]
    pedazo2 = lista[n + 1:long]
    print("Estos son los 2 arreglos resultantes al dividirlo por la mitad",end="")
    print(pedazo,end="")
    print(pedazo2,end="")
def concatenal(lista,long):
    """Pega 2 listas sacadas a partir de una lista principal, donde primero se deja la lista desde la mitad hasta el finall y después la lista desde el inicio a la mitad
    (list) -> list
    """
    n = (long // 2)
    pedazo = lista[0:n + 1]
    pedazo2 = lista[n + 1:long]
    lista3 = pedazo2 + pedazo
    print("")
    print("Esta es la lista pegada, conformada por las 2 anteriores",lista3)
def menor(lista):
    """Arroja el menor valor de una lista
    (list) -> int
    """
    print("Este es el valor más pequeño de la lista",min(lista))
def mayor(lista):
    """Arroja el valor más grande de una lista
    (list) -> int
    """
    print("Este es el valor más grande de la lista",max(lista))
def buscador(lista,long,buscar):
    """Busca si un valor está en una lista
    (list) -> bool
    """
    esta = False
    for i in range (0,long):
        if lista[i] == buscar:
            esta = True
    if esta:
        print("Su valor si se encuentra en la lista")
    else:
        print("Su valor no se encuentra en la lista")
def pos_buscador(lista,long,buscar):
    """Busca un elemento en la lista y dice su posición
    (list,int) -> int
    """
    for i in range (long):
        if lista[i] == buscar:
            return i     
def cambio(lista,long,posicion,valor):
    """Cambia el valor de una posición determinada
    (list) -> list
    """
    for i in range (long):
        if i == posicion:
            lista[i] = valor
    return lista
def eliminar(lista):
    """Elimina el último valor de una lista
    (list) -> list
    """
    lista_n = lista.copy()
    lista_n.pop()
    return(lista_n)
def eliminar2(lista,posicion):
    """Elimina el valor de una posición dada
    (list) -> list
    """
    lista.pop(posicion)
    return lista
def añadir(lista,posicion,valor):
    """Añade un valor a una posición dada 
    (int) -> list
    """
    lista.insert(posicion,valor)
    return lista
def añadir2(lista,valor):
    """Añade un valor a la lista en la primera posición
    (list) -> list
    """
    lista.insert(0,valor)
    return lista
def añadir3(lista,valor):
    """Añade un valor al final de la lista
    (list) -> list
    """
    lista.append(valor)
    return lista
def lista_pro(lista,long):
    """Imprime una lista, pero en lugar de llaves lleva corchetes y separa los valores con comas
    (list) -> list
    """
    print("{",end="")
    for i in range (long - 1):
        print(lista[i],",",end="")
    print(lista[-1],"}")
def inversa(lista):
    """Retorna la lista dada la vuelta
    (list) -> list
    """
    lista = lista[::-1]
    return lista
def lista_pro2(lista,long):
    """Imprime los valores de una lista, separados por espacios y sin llaves
    (list) -> list
    """
    for i in range (long - 1):
        print(lista[i]," ",end="")
    print(lista[-1])
def sumatoria(lista,long):
    """Si la lista es de valores enteros o flotantes, suma los valores con un ciclo y arroja el resultado
    (list) -> int
    """
    sumatoria = 0
    for i in range(long):
        sumatoria = sumatoria + lista[i]
    return sumatoria
def sumatoria2(suma,lista,cont,long):
    """Si la lista es de valores enteros o flotantes, suma los valores de forma recurrente y da el resultado
    (list) -> int
    """
    if cont < long:
        suma = suma + lista[cont]
        return sumatoria2(suma,lista,cont + 1,long)
    else:
        return suma
def intercambio(lista,long,posicion1,posicion2):
    """Intercambia 2 valores de una lista, la posición de estos valores debe ser dada
    (list) -> list
    """
    for i in range(long):
        if i == posicion2:
            aux = lista[i]
            lista[i] = lista[posicion1]
            lista[posicion1] = aux  
    return lista
def copia(lista):
    """Genera una copia de una lista
    (list) -> list
    """
    copia = lista.copy()
    return copia
def main():
    """Lee una serie de datos separados por comas y los pone en una lista mientras los convierte en entero
    (str) -> int
    """
    suma = 0
    cont = 0
    entrada = input("Ingrese los valores para el arreglo")
    lista = entrada.split(",")
    long = len(lista)
    valida_dato(lista,long)
    if all(isinstance(i,int) or isinstance(i,float)
    for i in lista):
        print("Estos son los valores organizados en una lista",lista)
        espaciados(lista,long)
        linea1(lista,long)
        elementos(long)
        pares(lista,long)
        print ("Esta es la cantidad de números pares en el arreglo:",pares(lista,long))
        mitades(lista,long)
        print("Este es el arreglo tomando los valores desde la mitad hasta el final",mitades(lista,long))
        pos_pares(lista,long)
        print("Estos son los valores que hay en las posiciones pares del arreglo",pos_pares(lista,long))
        mitades2(lista,long)
        concatenal(lista,long)
        menor(lista)
        mayor(lista)
        pregunta = input("¿Desea buscar algún valor en la lista?(Si/No)")
        if pregunta == "Si":
            buscar = int(input("¿Que valor desea buscar?"))
            buscador(lista,long,buscar)
            pos_buscador(lista,long,buscar)
            print("Su valor está en la posición",pos_buscador(lista,long,buscar))
        
        pregunta2 = input("¿Desea cambiar el valor de alguna posición?(Si/No)")
        if pregunta2 == "Si":
            posicion= int(input("¿Que posicón desea cambiar?"))
            valor = input("¿A que valor desea cambiar?")
            cambio(lista,long,posicion,valor)
            print("Esta es la nueva lista con el valor cambiado",cambio(lista,long,posicion,valor))

        print("Esta es la lista sin el último valor",eliminar(lista))
        pregunta3 = input("¿Desea eliminar el valor de alguna posición?(Si/No)")
        if pregunta3 == "Si":
            posicion = int(input("¿Que posición de la lista desea eliminar?"))
            print("Esta es la lista sin el valor que se eliminó",eliminar2(lista,posicion))

        pregunta4 = input("¿Quiere agregar algun valor a la lista en una posición específica?(Si/No)")
        if pregunta4 == "Si":
            posicion = int(input("¿En que posición desea agregar este valor?"))
            valor = int(input("¿Que valor desea agregar?"))
            print("Esta es la nueva lista con el valor agregado en esa posición",añadir(lista,posicion,valor))
        
        pregunta5 = input("¿Desea agregar un valor a la primera posición?(Si/No)")
        if pregunta5 == "Si":
            valor = input("¿Que valor desea ingresar a la lista en la primera posición?")
            print("Esta es la nueva lista con el valor agregado en la primera posición",añadir2(lista,valor))
        
        pregunta6 = input("¿Dese agregar un nuevo valor a la lista?(Si/No)")
        if pregunta6 == "Si":
            valor = input("¿Que valor desea agregar a la lista?")
            print("Esta es la nueva ista con el valor agregado",añadir3(lista,valor))
        lista_pro(lista,long)
        print("Esta es la lista invertida",inversa(lista))
        lista_pro2(lista,long)
        print("La suma de los elementos de la lista tiene como resultado:",sumatoria(lista,long))
        print("La suma de los elementos de la lista de manera recurrente tiene como resultado:",sumatoria2(suma,lista,cont,long))
        pregunta7 = input("¿Desea intercambiar el valor de 2 posiciones de la lista?(Si/No)")
        if pregunta7 == "Si":
            posicion1 = int(input("¿Cual es la primera posición que desea intercambiar?"))
            posicion2 = int(input("¿Cual es la segunda posición que desea intercambiar?"))
            print("Esta es la lista con los valores de las 2 posiciones intercambiadas",intercambio(lista,long,posicion1,posicion2))
        print("Esta es la copia de la lista",copia(lista))
    elif all(isinstance(i,str)
    for i in lista):
        print("Estos son los valores organizados en una lista",lista)
        espaciados(lista,long)
        linea1(lista,long)
        mitades(lista,long)
        print("Este es el arreglo tomando los valores desde la mitad hasta el final",mitades(lista,long))
        pos_pares(lista,long)
        print("Estos son los valores que hay en las posiciones pares del arreglo",pos_pares(lista,long))
        mitades2(lista,long)
        concatenal(lista,long)
        menor(lista)
        mayor(lista)
        pregunta = input("¿Desea buscar algún valor en la lista?(Si/No)")
        if pregunta == "Si":
            buscar = input("¿Que valor desea buscar?")
            buscador(lista,long,buscar)
            pos_buscador(lista,long,buscar)
            print("Su valor está en la posición",pos_buscador(lista,long,buscar))
        
        pregunta2 = input("¿Desea cambiar el valor de alguna posición?(Si/No)")
        if pregunta2 == "Si":
            posicion= int(input("¿Que posicón desea cambiar?"))
            valor = input("¿A que valor desea cambiar?")
            cambio(lista,long,posicion,valor)
            print("Esta es la nueva lista con el valor cambiado",cambio(lista,long,posicion,valor))

        print("Esta es la lista sin el último valor",eliminar(lista))
        pregunta3 = input("¿Desea eliminar el valor de alguna posición?(Si/No)")
        if pregunta3 == "Si":
            posicion = int(input("¿Que posición de la lista desea eliminar?"))
            print("Esta es la lista sin el valor que se eliminó",eliminar2(lista,posicion))

        pregunta4 = input("¿Quiere agregar algun valor a la lista en una posición específica?(Si/No)")
        if pregunta4 == "Si":
            posicion = int(input("¿En que posición desea agregar este valor?"))
            valor = (input("¿Que valor desea agregar?"))
            print("Esta es la nueva lista con el valor agregado en esa posición",añadir(lista,posicion,valor))
        
        pregunta5 = input("¿Desea agregar un valor a la primera posición?(Si/No)")
        if pregunta5 == "Si":
            valor = input("¿Que valor desea ingresar a la lista en la primera posición?")
            print("Esta es la nueva lista con el valor agregado en la primera posición",añadir2(lista,valor))
        
        pregunta6 = input("¿Dese agregar un nuevo valor a la lista?(Si/No)")
        if pregunta6 == "Si":
            valor = input("¿Que valor desea agregar a la lista?")
            print("Esta es la nueva ista con el valor agregado",añadir3(lista,valor))
        
        lista_pro(lista,long)
        print("Esta es la lista invertida",inversa(lista))
        lista_pro2(lista,long)
        pregunta7 = input("¿Desea intercambiar el valor de 2 posiciones de la lista?(Si/No)")
        if pregunta7 == "Si":
            posicion1 = int(input("¿Cual es la primera posición que desea intercambiar?"))
            posicion2 = int(input("¿Cual es la segunda posición que desea intercambiar?"))
            print("Esta es la lista con los valores de las 2 posiciones intercambiadas",intercambio(lista,long,posicion1,posicion2))
        print("Esta es la copia de la lista",copia(lista))
    else:
        print("Los valores son de diferente tipo, por favor introduzca todos los valores del mismo tipo")
main()

