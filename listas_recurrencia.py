
n = int(input("Cuantos valores desea ingresar"))
lista = []
cont = 0
m = n
while cont < n:
    entrada = int(input("n"))
    lista.append(entrada)
    cont = cont + 1
lista = sorted(lista)
print(lista)
m = n // 2
if n % 2 == 0:
    promedio = lista[m - 1] + lista[m]
    print (promedio / 2)

else:
    print(lista[m - 1])



