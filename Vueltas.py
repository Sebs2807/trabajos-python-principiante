#Trabajo vueltas condicionales
#Juán Sebastián Velásquez Rodríguez

total = int(input("¿Cual es el valor de su compra?"))
operacion = total // 200
if operacion != 0:
    print("Estas cantidad de billetes de 200:", operacion)
total = total - operacion*200

operacion = total // 100
if operacion != 0:
    print("Estas cantidad de billetes de 100:", operacion)
total = total - operacion*100

operacion = total // 50
if operacion != 0:
    print("Estas cantidad de billetes de 50:", operacion)
total = total - operacion*50

operacion = total // 20
if operacion != 0:
    print("Estas cantidad de billetes de 20:", operacion)
total = total - operacion*20

operacion = total // 2
if operacion != 0:
    print("Estas cantidad de monedas de 2:", operacion)
total = total - operacion*2

operacion = total // 1
if operacion != 0:
    print("Estas cantidad de monedas de 1:", operacion)
total = total - operacion*1







