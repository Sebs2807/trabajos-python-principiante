n = input("Ingrese nùmero hasta el que desea hacer la serie")
numero = int(n)
while numero > 0:
    print(n,end="")
    numero = numero - 1
    numerostr = str(numero)
    n = n + numerostr
