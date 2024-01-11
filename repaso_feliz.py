def feliz(valor):
    """Revisa si un número es feliz
    (int) -> bool
    """
    feliz = False
    valor = str(valor)
    suma = 0
    cont = 0
    while valor != "1":
        for i in range(len(valor)):
            suma = suma + (int(valor[i]) * int(valor[i]))
        valor = str(suma)
        cont += 1
        suma = 0
        if cont > 1000:
            return feliz
    feliz = True
    return True
def ordenamiento(lista):
    """Ordena una lista 
    (list) -> list
    """
    for i in range(1,len(lista)):
        valor = lista[i]
        indice = i
        while indice > 0 and lista[indice - 1] > valor:
            lista[indice] = lista[indice - 1]
            indice -= 1
        lista[indice] = valor
    return lista
def main():
    lista = []
    while True:
        valor = input("Ingrese el número (presione Enter para finalizar): ")
        if valor == "":
            break
        lista.append(int(valor))
    lista = ordenamiento(lista)
    final = []
    for i in range(len(lista)):
        if feliz(lista[i]):
            final.append(str(lista[i]))
    print(",".join(final))
main()