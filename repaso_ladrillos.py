def revisador(lista):
    """Revisa los valores de una lista y retorna el primero, junto con los que sean picos
    (list) -> list
    """
    final = []
    for i in range(len(lista) - 1):
        if lista[i] < lista[i + 1]:
            final.append(i + 2)
    if 1 not in final:
        final.insert(0,1)
    cantidad = len(final)
    return cantidad,final
def main():
    lista = input("Ingrese los valores de pila de ladrillos ").split(",")
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    cantidad,final = revisador(lista)
    print(cantidad)
    print(final)
main()