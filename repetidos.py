def revisador(lista,cont):
    """Función que revisa cuantas veces se repite un número en un arreglo
    (list) -> int
    """   
    long = len(lista)
    for i in range(cont - 1,long):
        revisar = lista.count(lista[i])
        if revisar >= 2:
            return lista[i]
def main():
    """Función que llama a los valores para el arreglo y llama a las demás funciones
    (list) -> list
    """
    final = []
    arreglo = input("Digite la secuencia en la que quiere ver que valores se repiten, separe los valores con espacios")
    lista = arreglo.split(" ")
    cont = 0
    for i in range(len(lista)):
        cont += 1
        if revisador(lista,cont) == None:
            continue
        else:
            if revisador(lista,cont) in final:
                continue 
            else:
                final.append(revisador(lista,cont))
    if len(final) == 0:
        print("Ningún valor se repite")
    else:
        print(final)

main()
        



        