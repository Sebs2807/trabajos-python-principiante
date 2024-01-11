def valor_absoluto(n):
    """Da el valor absoluto de un numero n
    (int,int) -> int
    """

    if n < 0:
        n = n * -1

    else:
        n = n

    return n

def mayor_valor(a,b,c):
    """Da el mayor valor entre 3 números
    (int,int,int) ->
    """

    if a > b:
        mayor = a
        if a > c:
            mayor = a

        else:
            mayor = c

    if b > a:
        mayor = b
        if b > c:
            mayor = b

        else:
            mayor = c

    if c > a:
        mayor = c
        if c > b:
            mayor = c

        else:
            mayor = b

    return mayor

def main():
    """Da el mayor valor entre 3 números, si los números son negativos, se tomará su valor absoluto
    (int,int,int) -> int
    """

    a = valor_absoluto(int(input("Digite el primer número")))
    

    b = valor_absoluto(int(input("Digite el segundo número")))
  

    c = valor_absoluto(int(input("Digite el tercer número")))
   

    return mayor_valor(a,b,c)
main()
