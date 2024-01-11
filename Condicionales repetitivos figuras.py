#Tarea condicionales repetitivos
#Juan Sebastián Velásquez Rodriguez

figura = input("Bienvenido, elija la figura que desea que dibuje la tortuga, las opciones son:triangulo, cuadrado, hexagono y estrella")
from turtle import *
shape("turtle")


if figura == "triangulo":
    numero = 0
    while numero < 3:
        forward(100)
        rt(120)
        numero = numero + 1
    print("Por favor revisar la nueva ventana de python que se abrió")
    
if figura == "hexagono":
    numero = 0
    while numero < 6:
        forward(100)
        rt(60)
        numero = numero + 1
    print("Por favor revisar la nueva ventana de python que se abrió")

if figura == "cuadrado":
    numero = 0
    while numero < 4:
        forward(100)
        rt(90)
        numero = numero + 1
    print("Por favor revisar la nueva ventana de python que se abrió")

if figura == "estrella":
    numero = 0
    while numero < 5:
        forward(100)
        rt(145)
        numero = numero + 1
    print("Por favor revisar la nueva ventana de python que se abrió")






    

