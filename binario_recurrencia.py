def binario(n,resultado):
    """Convierte un número que está en base 10 a base 2
    (int) -> int
    """
    mod = n % 2
    if mod == 0:
        resultado = "0" + resultado
    
    if mod == 1:
        resultado = "1" + resultado 

    if n == 1:
        print ("Este es su número en binario", resultado)
        return resultado
    
    if n == 0:
        print ("Este es su número en binario", 0)
        

    else:
        return binario(n // 2,resultado)
    

    

def main():
    """Recibe el número a cambiar de base 10 a base 2
    (int) -> int
    """
    n = int(input("Ingrese el número que desea convertir a binario"))
    resultado = ""
    binario(n,resultado) 
main()



