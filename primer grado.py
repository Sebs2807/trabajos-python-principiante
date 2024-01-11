def solución(a,b):
    """Resuelve ecuaciones de primer grado de la forma ax + b = 0
    (float,float) -> float
    """

    if a != 0:
        x = -b/a

    if a == 0 and b != 0:
        x = print("Imposible")

    if a == 0 and b == 0:
        x = print("Indeterminado")

    return x
