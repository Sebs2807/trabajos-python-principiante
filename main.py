#-----------------------------Importaciones---------------------------
import proyecto_matrices as pr
#------------------------Función principal-----------------------------
def punto1():
    """Lee y almacena valores ingresados por filas, en una matriz"""
    filas,columnas = input("Ingrese tamaño de la matriz ").split(",")
    matriz = pr.creamatriz(filas,columnas)
    matriz = pr.validadato(matriz)
    #Impresión punto 1
    print("----------------------------------")
    print("La matriz resultante es:")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == int(columnas) - 1:
                print(matriz[i][j])
            else:
                print(matriz[i][j],end =",")
    print("----------------------------------")
def punto2():
    """Genera un arreglo de dimensiones dadas, llena toda las posiciones con un valor dado"""
    filas,columnas,valor = input("Ingrese tamaño de la matriz, seguido del valor del que desea llenar la matriz ").split(",")
    llena = pr.rellenamatriz(filas,columnas,valor)
    #Impresión punto 2
    print("----------------------------------")
    print("La matriz resultante es:")
    for i in range(len(llena)):
        for j in range(len(llena[i])):
            if j == int(columnas) - 1:
                print(llena[i][j])
            else:
                print(llena[i][j],end=",")
    print("----------------------------------")
def punto3():
    """Ordenar descendentemente los valores de una matriz"""
    filas,columnas = input("Ingrese tamaño de la matriz ").split(",")
    matriz = pr.creamatriz(filas,columnas)
    matriz = pr.validadato(matriz)
    # Impresión punto 3
    print("----------------------------------")
    print("La matriz resultante es:")
    ordenada = pr.ordenamatriz(filas,columnas,matriz)
    for i in range(len(ordenada)):
        for j in range(len(ordenada[i])):
            if j == int(columnas) - 1:
                print(ordenada[i][j])
            else:
                print(ordenada[i][j],end=",")
    print("----------------------------------")
def punto4():
    """Entrega un vector con los valores arriba de la diagonal principal de una matriz"""
    filas,columnas = input("Ingrese tamaño de la matriz ").split(",")
    matriz = pr.creamatriz(filas,columnas)
    matriz = pr.validadato(matriz)
    valores = pr.arribadiago(matriz,filas)
    #Impresión punto 4
    if filas != columnas:
        print("Su matriz no es cuadrada")
    else:
        print("----------------------------------")
        print("Los valores son por encima de la diagonal son:")
        for i in range(len(valores)):
            if i == len(valores) - 1:
                print(valores[i])
            else:
                print(valores[i],end = ",")
        print("----------------------------------")
def punto5():
    """Dice el mayor valor de una matriz"""
    filas,columnas = input("Ingrese tamaño de la matriz ").split(",")
    matriz = pr.creamatriz(filas,columnas)
    matriz = pr.validadato(matriz)
    # Impresión punto 5
    print("----------------------------------")
    print("El mayor valor es:",pr.mayor(matriz,filas,columnas))
    print("----------------------------------")
def punto6():
    """Busca un valor en una matriz"""
    filas,columnas = input("Ingrese tamaño de la matriz ").split(",")
    matriz = pr.creamatriz(filas,columnas)
    matriz = pr.validadato(matriz)
    valor = input("¿Que valor desea buscar en la matriz?")
    try:
        valor = int(valor)
    except:
        valor = float(valor)
    pos1,pos2 = pr.buscavalor(matriz,valor)
    #Impresión punto 6
    print("----------------------------------")
    if not pos1 and not pos2:
        print("Su valor no está en la lista")
    else:
        print("Su valor está en la posición: ",pos1,",",pos2)
    print("----------------------------------")
def punto7():
    """Entrega la suma de los valores de la diagonal secundaria de una matriz"""
    filas, columnas = input("Ingrese el número de filas y columnas, separados por coma ").split(",")
    matriz = pr.creamatriz(filas,columnas)
    matriz = pr.validadato(matriz)
    print("La matriz ingresada es:")
    for fila in matriz:
        print(fila)
    suma = pr.sumadiagonal(matriz,filas)
    #Impresión punto 7
    print("----------------------------------")
    if suma is None:
        print("La matriz no es cuadrada.")
    else:
        print("La suma de la diagonal secundaria es:",suma)
    print("----------------------------------")
def punto8():
    """Encuentra los valores alrededor de una posición dada de una matriz"""
    filas,columnas = input("Ingrese tamaño de la matriz ").split(",")
    matriz = pr.creamatriz(filas,columnas)
    matriz = pr.validadato(matriz)
    pos1,pos2 = input("¿Que posición desea ver los valores alrededor?(separar la fila y columna con coma) ").split(",")
    vector = pr.ubicador(matriz,pos1,pos2,filas,columnas)
    #Impresión punto 8
    print("----------------------------------")
    print("Los valores alrededor de la posición seleccionada són: ")
    for i in range(len(vector)):
        if i == len(vector) - 1:
            print(vector[i])
        else:
            print(vector[i],end = ",")
    print("----------------------------------")
def punto9():
    """Entregar un vector con la suma de los valores en cada columna de una matriz"""
    filas,columnas = input("Ingrese tamaño de la matriz ").split(",")
    matriz = pr.creamatriz(filas,columnas)
    matriz = pr.validadato(matriz)
    sumatoria = pr.sumacolumnas(matriz,int(filas),int(columnas))
    #Impresión punto 9
    print("---------------------------------------------")
    print("La suma de las columnas de la matriz es:",end=" ") 
    for i in range(len(sumatoria)):
            if i == len(sumatoria) - 1:
                print(sumatoria[i])
            else:
                print(sumatoria[i],end = ",")
    print("---------------------------------------------")
def punto10():
    """Decir si una matriz cuadrada es la identidad"""
    filas,columnas = input("Ingrese tamaño de la matriz ").split(",")
    matriz = pr.creamatriz(filas,columnas)
    matriz = pr.validadato(matriz)
    identidad = pr.identidad(matriz,filas)
    # Impresión punto 10
    print("----------------------------------")
    if (int(filas) == 0 and int(columnas) == 0) or (int(filas) != int(columnas)):
        print("No es la matriz identidad, ya que la matriz no es cuadrada")
    else:
        if identidad:
            print("Si es la matriz identidad")
        else:
            print("No es la matriz identidad")
    print("----------------------------------")
def punto11():
    """Decir si una matriz es un cuadrado mágico"""
    filas,columnas = input("Ingrese tamaño de la matriz ").split(",")
    matriz = pr.creamatriz(filas,columnas)
    matriz = pr.validadato(matriz)
    if pr.magico(matriz,columnas):
        print("----------------------------------")
        print("Su matriz si es un cuadrado mágico")
        print("----------------------------------")
    else:
        print("----------------------------------")
        print("Su matriz no es un cuadrado mágico")
        print("----------------------------------")
def punto12():
    """Trasponer una matriz cuadrada"""
    filas,columnas = input("Ingrese tamaño de la matriz ").split(",")
    matriz = pr.creamatriz(filas,columnas)
    matriz = pr.validadato(matriz)
    matriz_nueva = pr.trasponer(matriz,int(filas))
    #Impresión punto 12
    print("----------------------------------")
    print("Su matriz traspuesta es:")
    for i in range(len(matriz_nueva)):
        for j in range(len(matriz_nueva[i])):
            if j == len(matriz_nueva[i]) - 1:
                print(matriz_nueva[i][j])
            else:
                print(matriz_nueva[i][j],end=",")
    print("----------------------------------")
def main():
    print("Se tienen las siguientes opciones de operaciones")
    while True:
        print("1. Leer y almacenar valores en una matriz ingresados por filas")
        print("2. Generar un arreglo de dimensiones dadas, llenar todas sus posiciones con un valor dado")
        print("3. Ordenar descendentemente los valores de una matriz")
        print("4. Entregar un vector con los valores arriba de la diagonal principal de una matriz")
        print("5. Entregar el mayor valor de una matriz")
        print("6. Buscar un valor dado en una matriz")
        print("7. Entregar la suma de los valores de la diagonal secundaria de una matriz")
        print("8. Encontrar los valores alrededor de una posición de la matriz")
        print("9 . Entregar un vector con la suma de los valores en cada columna de una matriz")
        print("10. Decir si una matriz cuadrada es la matriz identidad")
        print("11. Decir si una matriz es un cuadrado mágico")
        print("12. Trasponer una matriz cuadrada")
        print("13. Dejar de ejecutar")
        menu = input("¿Que operación desea realizar? ")
        if menu == "1":
            punto1()
        if menu == "2":
            punto2()
        if menu == "3":
            punto3()
        if menu == "4":
            punto4()
        if menu == "5":
            punto5()
        if menu == "6":
            punto6()
        if menu == "7":
            punto7()
        if menu == "8":
            punto8()
        if menu == "9":
            punto9()
        if menu == "10":
            punto10()
        if menu == "11":
            punto11()
        if menu == "12":
            punto12()
        if menu == "13":
            break
main()