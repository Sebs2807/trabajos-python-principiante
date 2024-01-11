#Trabajo conjuntos
#Juan Sebastian Velasquez y Sebastian Albarracin Silva

numero = int(input("Bienvenido, por favor introduzca un numero que quiera verificar si esta en alguno de los 2 intervalos"))
numero1 = int(input("Introduzca el numero inicial del primer intervalo"))
numero2 = int(input("Introduzca el numero final del primer intervalo"))
print("Su primer conjunto es:",[numero1,numero2])
numero3 = int(input("Introduzca el numero inicial del segundo intervalo"))
numero4 = int(input("Introduzca el numero final del segundo intervalo"))
print("Su segundo conjunto es:",[numero3,numero4])
  
if numero < numero2 and numero > numero1:
    print("Su numero esta en el intervalo",[numero1,numero2])
    conjunto1 = True
    y = False

elif numero >= numero2 or numero <= numero1:
    conjunto1 = False
    

if numero <= numero4 and numero >= numero3:
    print("Su numero esta en el intervalo",[numero3,numero4])
    conjunto2 = True

elif numero >= numero4 or numero <= numero3:
    conjunto2 = False
    x = True

if conjunto1 == True and conjunto2 != True:
    print(numero,"esta en la diferencia conjunto1 - conjunto2")

if y == True and conjunto1 or conjunto2 == True:
    print(numero,"esta en la union")
    x = False

if conjunto1 and conjunto2 == True:
    print(numero,"esta en la interseccion")


if x and y:
    print("Su numero no esta en ningun intervalo")

    
