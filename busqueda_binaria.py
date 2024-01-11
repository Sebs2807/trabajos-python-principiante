def busqueda(lista,buscar):
    """Busca mediante la busqueda binaria, un valor específico
    (list) -> str
    """
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    auxiliar = ""
    retornar = []
    while auxiliar != buscar:
        try:
            auxiliar = lista[len(lista)//2]
        except:
            return retornar, False
        if auxiliar > buscar:
            lista = lista[:len(lista)//2]
        else:
            lista = lista[len(lista)//2 + 1:]
        retornar.append(auxiliar)
    return retornar, True
def main():
    linea = input("¿Qué números de casas tiene?")
    lista = linea.split(",")
    buscar = int(input("¿Qué número de casa desea buscar?"))
    pasos,estar= busqueda(lista,buscar)
    if estar:
        for i in range(len(pasos)):
            print(pasos[i])
    else:
        for i in range(len(pasos)):
            print(pasos[i])
        print("Camila se fue a vivir a Tombuctu")
main()