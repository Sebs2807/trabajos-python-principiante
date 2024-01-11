def rimas(lista):
    """Revisa las últimas 2 letras de una palabra para saber cuales riman
    (list) -> list
    """
    rimas = []
    for i in range(len(lista)):
        rimas.append(lista[i][-2:])
    ordenamiento = False
    while not ordenamiento:
        ordenamiento = True
        for i in range(len(rimas) - 1):
            if rimas[i] > rimas[i + 1]:
                lista[i],lista[i + 1] = lista[i + 1],lista[i]
                ordenamiento = False
    for i in range(len(lista)):
        if lista[i][-]
def main():
    lista = []
    while True:
        valor = input("Ingrese la palabra (Ingrese enter para finalizar): ")
        if valor == "":
            break
        lista.append(valor)
    rimas(lista)
main()