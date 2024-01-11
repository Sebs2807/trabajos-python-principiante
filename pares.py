#pares menores
#Juan Sebastián Velásquez Rodríguez

def revisapar(a,b,c):
    """ De 3 números mira el menor de los valores pares
    (int, int, int) - > int
    """
    

    menor = 1
  
    if a % 2 == 0:
        menor = a
        if b % 2 == 0:
            if b < menor:
                menor = b
        if c % 2 == 0 and c < menor:
            menor = c

    else:
        if  b % 2 == 0:
            menor = b
        if c % 2 == 0 and c < menor:
            menor = c


    return menor  
  

def main():
    a = int(input("Ingrese primer número"))
    b = int(input("Ingrese segundo número"))
    c = int(input("Ingrese tercer número"))
    menor = revisapar(a,b,c)

    if menor == 1:
        print("No hay ningún valor par")

    else:
        print ("El menor valor par es:",menor)
    

main()
