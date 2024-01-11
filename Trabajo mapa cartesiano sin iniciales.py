#Trabajo mapa cartesiano
#Juán Sebastián Velásquez Rodríguez

x = int(input("Ingrese la coordenada x inicial que desea"))
y = int(input("Ingrese la coordenada x inicial que desea"))
input("Estas son las instrucciones posibles: up,ne,right,se,down,so,left,no.Coloque la instrucción y debajo el número de casillas a mover")
instrucción = input("¿Que instrucciones desea dar?")

if instrucción == "up":
    cambio = int(input("¿Cuantas casillas desea moverse?"))
    inicial = (x,y + cambio)
    print("Ahora se encuentra en",inicial)

if instrucción == "ne":
    cambio = int(input("¿Cuantas casillas desea moverse?"))
    inicial = (x + cambio,y + cambio)
    print("Ahora se encuentra en",inicial)

if instrucción == "right":
    cambio = int(input("¿Cuantas casillas desea moverse?"))
    inicial = (x + cambio,y)
    print("Ahora se encuentra en",inicial)

if instrucción == "se":
    cambio = int(input("¿Cuantas casillas desea moverse?"))
    inicial = (x + cambio,y - cambio)
    print("Ahora se encuentra en",inicial)

if instrucción == "down":
    cambio = int(input("¿Cuantas casillas desea moverse?"))
    inicial = (x,y - cambio)
    print("Ahora se encuentra en",inicial)

if instrucción == "so":
    cambio = int(input("¿Cuantas casillas desea moverse?"))
    inicial = (x - cambio,y - cambio)
    print("Ahora se encuentra en",inicial)

if instrucción == "left":
    cambio = int(input("¿Cuantas casillas desea moverse?"))
    inicial = (x - cambio,y)
    print("Ahora se encuentra en",inicial)

if instrucción == "no":
    cambio = int(input("¿Cuantas casillas desea moverse?"))
    inicial = (x - cambio,y + cambio)
    print("Ahora se encuentra en",inicial)
    
