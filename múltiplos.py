def multiplicador(n,cantidad):
    """Retorna una lista con los múltiplos del número dado
    (int,int) -> list
    """
    final = []
    for i in range(1,cantidad + 1):
        final.append(n * i)
    return final
def main():
    cantidad = int(input("Ingrese la cantidad de múltiplos que desea hallar"))
    n = int(input("Ingrese el número al que quiere hallarle los múltiplos"))
    for i in range(len(multiplicador(n,cantidad))):
        print(multiplicador(n,cantidad)[i],end=" ")
main()