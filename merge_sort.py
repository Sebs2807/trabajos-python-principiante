def partir(lista,lado = ""):
    """Función que divide lista en 2
    (list) -> list
    """
    if len(lista) <= 1: #caso base
        return lista
    else:
        mitad = len(lista) // 2
        izq = lista[:mitad]
        der = lista[mitad:]
        uno = partir(izq, "izquierdo") #caso reccurrente
        dos = partir(der, "derecho") #caso reccurrente
        nueva = mezclador(uno,dos)
        return nueva
def mezclador(lista1,lista2):
    """Mezcla 2 listas ya organizadas y retorna una lista organizada de las 2
    (list) -> list
    """
    n1 = len(lista1)
    n2 = len(lista2)
    ordenada = []
    l1 = 0
    l2 = 0
    while l1 < n1 and l2 < n2:
        if lista1[l1] < lista2[l2]:
            ordenada.append(lista1[l1])
            l1 += 1
        else:
            ordenada.append(lista2[l2])
            l2 += 1
    if l1 < n1:
        ordenada = ordenada + lista1[l1:]
    if l2 < n2:
        ordenada = ordenada + lista2[l2:]
    return ordenada
def generar(long):
    """Genera una lista de la longitud deseada
    (int) -> list
    """
    import random
    nueva = []
    for i in range(long):
        nueva.append(random.randrange(0,long*3))
    return nueva
def burbuja(lista):
    """Algoritmo ordenamiento de burbuja
    (list) -> list
    """
    while True:
        ordenar = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i],lista[i + 1] = lista[i + 1],lista[i]
                ordenar = True
        if not ordenar:
            return lista
def main():
    import time
    long = int(input("Digite longitud lista"))
    lista = generar(long)
    otra = lista.copy()
    inicio1 = time.time()
    partir(lista)
    fin1 = time.time()
    inicio2 = time.time()
    burbuja(otra)
    fin2 = time.time()
    print("El algoritmo merge se demoró:",fin1 - inicio1,"segundos")
    print("El algoritmo burbuja se demoró:",fin2 - inicio2,"segundos")
main()
