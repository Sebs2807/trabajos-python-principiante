#Ejercicio 21 cartas
#Juan Sebastian Velasquez Rodriguez

import random
from random import *
carta = randrange(1,11)
carta2 = randrange(1,11)
carta3 = 0
input("Bienvenido al juego de 21, si alguna de tus cartas es 10 o 1, podras elegir cambiarla para hacer un puntajer mayor o menor")
input("Estas son sus 2 cartas iniciales")
input(carta)
input(carta2)
pregunta = input("¿Desea otra carta? (si/no)")
#Preguntas al jugador
if pregunta.lower () == "si":
    carta3 = randrange(1,11)
    print("Esta es su tercera carta",carta3)
    print("Estos son tus puntos totales",(carta + carta2 + carta3))
if carta == 10:
    pregunta_2 = input("¿Quieres cambiar el valor de tu primera carta?(si/no)")
    if pregunta_2 == "si":
        carta = 1
        print("Ahora el valor de tu carta es",carta)
        print("Estos son tus puntos totales",(carta + carta2 + carta3))
elif carta == 1:
    pregunta_2 = input("¿Quieres cambiar el valor de tu primera carta?(si/no)")
    if pregunta_2 == "si":
        carta = 10
        print("Ahora el valor de tu carta es",carta)
        print("Estos son tus puntos totales",(carta + carta2 + carta3))
if carta2 == 10:
    pregunta_2 = input("¿Quieres cambiar el valor de tu segunda carta?(si/no)")
    if pregunta_2 == "si":
        carta2 = 1
        print("Ahora el valor de tu carta es",carta2)
        print("Estos son tus puntos totales",(carta + carta2 + carta3))
elif carta2 == 1:
    pregunta_2 = input("¿Quieres cambiar el valor de tu segunda carta?(si/no)")
    if pregunta_2 == "si":
        carta2 = 10
        print("Ahora el valor de tu carta es",carta2)
        print("Estos son tus puntos totales",(carta + carta2 + carta3))
if carta3 == 1:
    pregunta_2 = input("¿Quieres cambiar el valor de tu tercera carta?(si/no)")
    if pregunta_2 == "si":
        carta3 = 10
        print("Ahora el valor de tu carta es",carta3)
        print("Estos son tus puntos totales",(carta + carta2 + carta3))
elif carta3 == 10:
    pregunta_2 = input("¿Quieres cambiar el valor de tu tercera carta?(si/no)")
    if pregunta_2 == "si":
        carta3 = 1
        print("Ahora el valor de tu carta es",carta3)
        print("Estos son tus puntos totales",(carta + carta2 + carta3))

if (carta + carta2 + carta3) <= 21 :
    print("Bien jugado, te faltaron",(21 - (carta + carta2 + carta3)))
else:
    print("Buen intento, te sobraron",((carta + carta2 + carta3)-21))



    
    
          
