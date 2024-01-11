def ordenada_a(arreglo):
    """Retorna un valor booleando sobre si la lista está ordenada de manera ascedente
    (list) -> bool
    """
    cont = 0
    ordenado = True
    while ordenado:
        cont = cont + 1
        try:
            if int(arreglo[cont - 1]) > int(arreglo[cont]):
                ordenado = False
                return ordenado
        except IndexError:
            return ordenado

def ordenada_d(arreglo):
    """Retorna un valor booleando sobre si la lista está ordenada de manera descendente
    (list) -> bool
    """
    cont = 0
    ordenado = True
    while ordenado:
        cont = cont + 1
        try:
            if int(arreglo[cont - 1]) < int(arreglo[cont]):
                ordenado = False
                return ordenado
        except IndexError:
            return ordenado

def main():
    linea = input("Linea ")
    valores = linea.split(",")
    if ordenada_a(valores) == True and ordenada_d(valores) == False:
        print("Esta ordenada")
    elif ordenada_d(valores) == True and ordenada_a(valores) == False:
        print("Esta ordenada")
    else:
        print("Esta desordenada")

main()
