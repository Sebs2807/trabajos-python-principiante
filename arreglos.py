def main():
    arreglo = input("Digite la secuencia en la que quiere ver que valores se repiten, separe los valores con espacios")
    lista = arreglo.split(" ")
    long = len(lista)
    cont = 1
    revisar = lista[0]
    while cont < long:
        if lista[cont] == revisar:
            print(lista[cont])
            for i in range(long + 1):
                long = len(lista)
                try:
                    if lista[i] == revisar:
                        del lista[i]
                except IndexError:
                    break
            if cont + 1 < long:
                revisar = lista[cont + 1]
            cont = 0
        else:
            if cont + 1 < long:
                revisar = lista[cont + 1]
            cont += 1
    
main()