def revisador(lista):
    """Función que retorna una lista con los valores repetidos consecutivos eliminados
    (list) -> list
    """
    for i in range(len(lista)):
        try:
            if lista[i] == lista[i + 1]:
                del lista[i + 1]
                if lista[i] == lista[i - 1]:
                    del lista[i - 1]
        except IndexError:
            return lista
def main():
    linea = input("Ingrese la linea a la que quiere eliminarle los valores repetidos consecutivamente")
    lista = linea.split(" ")
    revisador(lista)
    print("Esta es la secuencia sin los valores consecutivos repetidos")
    for i in range(len(revisador(lista))):
        print(revisador(lista)[i],end=" ")
main()