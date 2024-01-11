def posiciones(lista):
    """De una lista mira las posiciones en las que al sumar los valores anteriores da 0
    (list) -> int
    """
    suma = lista[0]
    final = []
    for i in range(1, len(lista)):
        suma = lista[i] + suma
        if suma == 0 and i != len(lista) -1:
            final.append(i + 1)
    cantidad = len(final)
    return final, cantidad
def main():
    lista = input("Ingrese la linea con la cantidad de perros ").split(",")
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    final,cantidad = posiciones(lista)
    if cantidad == 0:
        print("OK")
    else:
        print(cantidad)
        for i in range(len(final)):
            print(final[i])
main()