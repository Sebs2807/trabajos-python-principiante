def revisador(lista):
    """Retorna una lista, la cual es el extremo derecho de la lista original si es bitónica
    (list) -> list
    """
    final = []
    for i in range(1,len(lista)):
        if i == len(lista) - 1:
            if lista[-1] > lista[i - 1]:
                return final
        if lista[i] < lista[i - 1]:
            pos = i - 1
    final = lista[pos - 1:]
    return final
def revisador2(arreglo,lista):
    """Revisa la lista resultante y si es completamente descendente, retorna una bandera con valor True
    (list) -> bool
    """
    arreglo = revisador(lista)
    b = True
    for i in range(1,len(arreglo)):
        if arreglo[i] > arreglo[i - 1]:
            b = False
    return b
def main():
    linea = input("Ingrese la linea que quiere saber si es bitónica")
    lista = linea.split(",")
    final = revisador(lista)
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    if revisador2(final,lista):
        print("Es bitónica")
    if not revisador2(final,lista):
        print("No es bitónica")
main()