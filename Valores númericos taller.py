def modifica_val(a,n):
    mn = menor (a,n)
    my = mayor (a,n)
    for i in range (0,n):
        a[i] = round ((a[i] - mn) / (my - mn),1)
    
    return a
def menor (a,n):
    mn = a[0]
    for i in range (1,n):
        if a[i] < mn:
            mn = a[i]
    return mn

def mayor (a,n):
    my = a[0]
    for i in range (1,n):
        if a[i] > my:
            my = a[i]
    return my

def main():
    linea = input("Valores numéricos para el arreglo")
    datos = linea.split(",")
    n = len(datos)
    for i in range (0,n):
        datos[i] =float(datos[i])
    datos = modifica_val(datos,n)
    print(datos)

main()
    

