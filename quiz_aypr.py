##Juan Sebastián Velásquez Rodríguez
##Quiz aypr
#Funcion que busca el numero
def buscador(lista,valor):
    """Funcion que retorna una lista, cuyos valores, son las posiciones de un valor en una lista
    (list,int) -> list
    """
    posiciones = []
    for i in range(len(lista)):
        if lista[i] == valor:
            posiciones.append(i)
    return posiciones

#Funcion principal     
def main():
    linea = input("Ingrese la linea de valores separados por coma")
    valor = input("¿Qué valor desea encontrar las posiciones/posición donde esta?")
    lista = linea.split(",")
    for i in range(len(buscador(lista,valor))):
        if i == len(buscador(lista,valor))-1:
            print(buscador(lista,valor)[i],end="")
        else:
            print(buscador(lista,valor)[i],end="")
            print(",",end="")
main()
    
