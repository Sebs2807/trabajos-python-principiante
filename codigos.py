def revisa_num(lineanum):
    """Revisa en una secuencia el número mayor y retorna la posición
    (list) -> int
    """
    posm = 0
    for i in range(len(lineanum)):
        for j in range(len(lineanum)):
            if lineanum[j] > lineanum[i]:
                posm = j
            else:
                posm = posm
    return posm
def revisa_let(linealet,lineanum):
    """Revisa la posición de la secuencia de números y retorna la letra en esa posición
    (int) -> str
    """
    pos = revisa_num(lineanum)
    for i in range(len(linealet)):
        if i == pos:
            return linealet[i]
def main():
    line1 = input("Ingrese la secuencia de letras")
    linealet = line1.split(",")
    linea2 = input("Ingrese la secuencia de números")
    lineanum = linea2.split(",")
    for i in range(len(lineanum)):
        lineanum[i] = int(lineanum[i])
    revisa_num(lineanum)
    print("Esta es la letra que está en la posición del número mayor:",revisa_let(linealet,lineanum))
main()