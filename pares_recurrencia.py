def pares (n,par):
    """Retorna los digitos pares de un número entero
    (int) -> int
    """

    revisar = n % 10
    mod = revisar % 2

    if n == 0:
        print ("La cantidad de números pares es:",par)
        return par

    if mod == 0:
        par = par + 1
        return pares(n // 10,par)

    if mod != 0:
        par = par
        return pares (n // 10,par)
    

    
def main():
    """Dice la cantidad de números pares que hay en un número entero n
    (int) -> int
    """
    par = 0
    n = int(input("Ingrese el número en el que desea saber cuantos números pares hay"))
    if n == 0:
        par = 1
    return pares(n,par)
main()

