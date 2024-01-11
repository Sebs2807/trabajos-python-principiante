def generar(longitud):
    """Genera una lista con valores aleatorios entre 0 y la longitud de la lista multiplicada por 3
    (int) -> list
    """
    lista = []
    from random import randrange
    for i in range(longitud):
        lista.append(randrange(0,longitud * 3))
    return lista
def main():
    longitud = int(input("¿Qué longitud desea para la lista?"))
    print (generar(longitud))
main()