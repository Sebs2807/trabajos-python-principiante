def revisador(lista,cont):
    """Función que revisa cuantas veces se repite un número en un arreglo
    (list) -> int
    """   
    long = len(lista)
    for i in range(cont - 1,long):
        revisar = lista.count(lista[i])
        if revisar >= 2:
            return True
def main():
    """Función que llama a los valores para el arreglo y llama a las demás funciones
    (list) -> list
    """
    arreglo = input("Digite la secuencia en la que quiere ver si hay valores repetidos, separe los valores con comas")
    lista = arreglo.split(",")
    cont = 0
    for i in range(len(lista)):
        cont += 1
        if revisador(lista,cont) == None:
            print (False)
            break
        else:
             if revisador(lista,cont) == True:
                 print(revisador(lista,cont))
                 break
    
main()