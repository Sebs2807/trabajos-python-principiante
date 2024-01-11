def posiciones(arreglo):
    """Función que revisa que edades son mayores a 18
    (list) -> list
    """
    nueva = []
    for i in range(len(arreglo)):
        if arreglo[i] >= 18:
            nueva.append(i)
    return nueva 
def main():
    nombres = []
    edades = []
    continua = True
    while continua:
        nombre = input("Digite nombre")
        edad = int(input("Digite edad"))
        nombres.append(nombre)
        edades.append(edad)
        resp = input("Digite 1 para continuar o enter para terminar")
        if resp != "1":
            continua = False
    pos = posiciones(edades)
    nombres_m = []
    edades_m = []
    for i in range(len(pos)):
        nombres_m.append(nombres[pos[i]])
        edades_m.append(edades[pos[i]])
    print(nombres_m)
    print(*edades_m)
main()
    