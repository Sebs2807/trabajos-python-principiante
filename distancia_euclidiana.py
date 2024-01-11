def diferencia(lista1,lista2):
    sumatoria = 0
    listaf = []
    for i in range(len(lista1)):
        diferencia = abs(lista1[i] - lista2[i])
        listaf.append(diferencia)
    for i in range(len(listaf)):
        sumatoria = sumatoria + listaf[i]**2
    return sumatoria

def main():
    import math 
    arreglo1 = input("Ingrese el primer vector para hallar la distancia euclidiana")
    lista1 = arreglo1.split(",")
    for i in range(len(lista1)):
        lista1[i] = int(lista1[i])
    arreglo2 = input("Ingrese el segundo vector para hallar la distancia euclidiana")
    lista2 = arreglo2.split(",")
    for i in range(len(lista2)):
        lista2[i] = int(lista2[i])
    resultado = math.sqrt(diferencia(lista1,lista2))
    print(round(resultado,2))
main()



