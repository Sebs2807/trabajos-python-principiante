def Kaprekar(valor):
    """Revisa un número cumple la propiedad de ser un número de Kaprekar
    (list) -> bool
    """
    kapreka = False
    nuevo = str(valor * valor)
    for i in range(len(nuevo)):
        try:
            if (int(nuevo[:i + 1]) + int(nuevo[i + 1:])) == valor:
                kapreka = True
                return kapreka
        except:
            continue
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
        if Kaprekar(lista[i]):
            final.append(str(lista[i]))
    print(",".join(final))
main()
