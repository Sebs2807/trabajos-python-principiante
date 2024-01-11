#Programa bolardos
#Juan Sebastián Velásquez Rodríguez

def main():
    coma = ","
    bld = int(input("Ingrese altura bolardo"))
    mayor = bld
    diferenciaM = 0
    contador = 0
    n = 1

    
    if bld == -1:
        print("Error, no hubo datos")

    else:
        while bld != -1:
            bld = int(input("Ingrese altura bolardo"))
            dif = abs(mayor - bld)
            mayor = bld

            if dif > diferenciaM and bld != -1:
                diferenciaM = dif
                contador = contador + 1



        print(contador,contador + 1)

                
        
        
        
                

        


        
    
main()
