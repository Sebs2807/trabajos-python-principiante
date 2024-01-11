def revisador(lista):
    """Revisa en que posiciones están los picos en una secuencia
    (list) -> list
    """
    final = []
    for i in range(1,len(lista) - 1):
        if lista[i] > lista[i - 1] and lista[i] > lista[i + 1]:
            final.append(i)
    return final
def main():
    linea = input("Ingrese la linea a la que quiere hallarle los picos")
    lista = linea.split(",")
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    if len(revisador(lista)) == 0:
        print("No hay picos")
    for i in range(len(revisador(lista))):
        if i == len(revisador(lista)) - 1:
            print(revisador(lista)[i],end="")
        else:
            print(revisador(lista)[i],end="")
            print(",",end="")
main()