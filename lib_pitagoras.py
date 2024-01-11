

def pitagoras (lado1,lado2):
    """ Calcula la hipotenusa de un triángulo
    (float,float) -> float
    """

    import math
    hipotenusa = math.sqrt(lado1**2 + lado2**2)

    return hipotenusa

def potencia (n,m):
    """ Calcula de la potencia de un número n m veces
    (int,int) -> int
    """

    elevado = n**m

    return elevado

def esTriangular(lado1,lado2,lado3):
    """ Verifica si los lados ingresados, pueden corresponder a lados de un triángulo
    (float,float) -> float
    """

    if (lado1 + lado2) >= lado3:
        vv = True

    if (lado2 + lado3) >= lado1:
        vv = True

    if (lado1 + lado3) >= lado2:
        vv = True

    else:
        vv = False


    return vv

    

    




    

