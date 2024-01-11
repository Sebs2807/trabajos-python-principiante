#------------------------Funciones-----------------------#
def corrector(lista,columnas):
    """Revisa si la cantidad de valores que entran en una fila, es menor o igual que la cantidad de columnas
    (list2D,int) -> bool
    """
    if len(lista) > int(columnas):
        return False
    else:
        return True
def rellenador(lista,columnas):
    """Ingresa una lista correspondiente a la fila de una matriz, rellena la fila con 0 en caso de estar incompleta
    (list) -> list
    """
    while len(lista) < int(columnas):
        lista.append("0")
    return lista
def aplanamatriz(matriz,filas,columnas):
    """Pone una matriz en una sola fila
    (list2D,int,int) -> list
    """
    nueva = []
    for i in range(int(filas)):
        for j in range(int(columnas)):
            nueva.append(matriz[i][j])
    return nueva
def insercion(lista):
    """Ordena una lista mediante el método de inserción
    (list) -> list
    """
    for i in range(1,len(lista)):
        valor = lista[i]
        indice = i
        while indice > 0 and lista[indice - 1] < valor:
            lista[indice] = lista[indice - 1]
            indice -= 1
        lista[indice] = valor
    return lista
def validadato(matriz):
    """Revisa los datos de una matriz y los pone a todos en el mismo tipo
    (list2D) -> list2D
    """
    punto = False
    if len(matriz) == 0:
        return matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j].find(".") != -1:
                punto = True
                break
    if punto:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j] = float(matriz[i][j])
    if not punto:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j] = int(matriz[i][j])
    return matriz
def creamatriz(filas,columnas):
    """Crea una matriz con la cantidad de filas dada
    (int,int) -> list2D
    """
    matriz = []
    if int(columnas) == 0 or int(filas) == 0:
        return matriz
    cont = 0
    while cont < int(filas):
        linea = input("Ingrese la fila de la matriz ")
        fila = rellenador(linea.split(","),columnas)
        revisar = corrector(fila,columnas)
        if revisar:
            matriz.append(fila)
            cont += 1
        else:
            linea = input("Ingrese la fila de la matriz ")
            fila = rellenador(linea.split(","),columnas)
            revisar = corrector(fila,columnas)
            if revisar:
                matriz.append(fila)
                cont += 1
    return matriz
def ordenamatriz(filas,columnas,matriz):
    """Recibe una lista ordenada y la acomoda de forma que se vuuelva una matriz
    (int,int,list2D) -> list2D
    """
    aordenar = aplanamatriz(matriz,filas,columnas)
    lista_ord = insercion(aordenar)
    matriz_final = []
    a = 0
    for i in range(int(filas)):
        fila = []
        for j in range(int(columnas)):
            fila.append(lista_ord[a])
            a += 1
        matriz_final.append(fila)
    return matriz_final
def rellenamatriz(filas,columnas,valor):
    """Crea una matriz con un valor dado en todas las posiciones según el tamaño dado
    (int,int,int/float/str) -> list2D
    """
    matriz = []
    for i in range(int(filas)):
        fila = []
        for j in range(int(columnas)):
            fila.append(valor)
        matriz.append(fila)
    return matriz
def mayor(matriz,filas,columnas):
    """Retorna el mayor valor de una matriz
    (list2D,int,int) -> int/float
    """
    matriz = aplanamatriz(matriz,filas,columnas)
    matriz = insercion(matriz)
    return matriz[0]
def identidad(matriz,filas):
    """Revisa si una matriz cuadra es la matriz identidad
    (list2D,int) -> bool
    """ 
    identidad = True
    cont = 0
    while cont < int(filas):
        if matriz[cont][cont] != 1:
            identidad = False
        cont += 1
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i != j:
                if matriz[i][j] != 0:
                    identidad = False
    return identidad
def arribadiago(matriz,filas):
    """Retorna una lista con los valores por encima de la diagonal de una matriz cuadrada
    (list2D,int) -> list
    """
    valores = []
    for i in range(int(filas)):
        for j in range(len(matriz[i])):
            if i != j and j > i:
                valores.append(matriz[i][j])
    return valores
def sumadiagonal(matriz,filas):
    """Suma la diagonal secundaria de una matriz
    (list2D,int) -> int/float
    """
    for fila in matriz:
        if len(fila) != int(filas):
            return None 
    suma = 0
    for i in range(int(filas)):
        suma += matriz[i][int(filas)-1-i]
    return suma
def buscavalor(matriz,valor):
    """Busca un valor específico en una matriz
    (list2D,int/float) -> (int,int)/bool
    """
    pos1,pos2 = False,False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if valor == matriz[i][j]:
                pos1,pos2 = i,j
    return pos1,pos2
def magico(matriz,columnas):
    """Revisa si una matriz cumple ser un cuadrado mágico
    (list2D,int) -> bool
    """
    filas = len(matriz)
    cuadradomagico = True
    sumafilas = []
    sumacolumnas = []
    #Sumadora de filas
    suma1 = 0
    for i in range(filas):
        for j in range(len(matriz[i])):
            suma1 += matriz[i][j]
        sumafilas.append(suma1)
        suma1 = 0
    #Sumador de columnas
    sumacolumnas = [0] * int(columnas)
    for j in range(int(columnas)):
        sumacolumna = 0
        for i in range(filas):
            sumacolumna += matriz[i][j]
        sumacolumnas[j] = sumacolumna
    #Sumador de diagonal
    suma2 = 0
    for i in range(filas):
        for j in range(len(matriz[i])):
            if i == j:
                suma2 += matriz[i][j]
    if suma2 == sumafilas[0] and suma2 == sumacolumnas[0] and sumacolumnas == sumafilas:
        cuadradomagico = True
    else:
        cuadradomagico = False
    return cuadradomagico
def sumacolumnas(matriz,filas,columnas):
    """Suma las columnas de una matriz
    (list2D,int,int) -> int
    """
    sumacolumnas = [0] * columnas
    for j in range(columnas):
        sumacolumna = 0
        for i in range(filas):
            sumacolumna += matriz[i][j]
        sumacolumnas[j] = sumacolumna
    return sumacolumnas
def trasponer(matriz,filas):
    """Genera la traspuesta de una matriz
    (list2D,int) -> list2D
    """
    for fila in matriz:
        if len(fila) != filas:
            return None
    for i in range(filas):
        for j in range(i, filas):
            original = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = original
    return matriz
def ubicador(matriz,pos1,pos2,filas,columnas):
    """Mira los valores que hay alrededor de cierta posición en una matriz
    (list2D,int,int,int,int) -> list
    """
    pos1 = int(pos1)
    pos2 = int(pos2)
    vector = []
    if 0 <= pos1 - 1 < int(filas) and 0 <= pos2 - 1 < int(columnas):
        vector.append(matriz[pos1 - 1][pos2 - 1])
    if 0 <= pos1 - 1 < int(filas) and 0 <= pos2 < int(columnas):
        vector.append(matriz[pos1 - 1][pos2])
    if 0 <= pos1 - 1 < int(filas) and 0 <= pos2 + 1 < int(columnas):
        vector.append(matriz[pos1 - 1][pos2 + 1])
    if 0 <= pos1 < int(filas) and 0 <= pos2 - 1 < int(columnas):
        vector.append(matriz[pos1][pos2 - 1])
    if 0 <= pos1 < int(filas) and 0 <= pos2 + 1 < int(columnas):
        vector.append(matriz[pos1][pos2 + 1])
    if 0 <= pos1 + 1 < int(filas) and 0 <= pos2 - 1 < int(columnas):
        vector.append(matriz[pos1 + 1][pos2 - 1])
    if 0 <= pos1 + 1 < int(filas) and 0 <= pos2 < int(columnas):
        vector.append(matriz[pos1 + 1][pos2])
    if 0 <= pos1 + 1 < int(filas) and 0 <= pos2 + 1 < int(columnas):
        vector.append(matriz[pos1 + 1][pos2 + 1])
    return vector
