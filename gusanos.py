cantidad = int(input())
lista1 = input()
gusanos = lista1.split(" ")
intervalos = []
for i in range(0,cantidad):
    intervalos.append(int(gusanos[i]))
    intervalos[i] = intervalos[i - 1] + intervalos[i]

revisiones = int(input())
lista2 = input()
valores = lista2.split(" ")
for i in range(len(valores)):
    valores[i] = int(valores[i])
nueva = valores.copy()
valores = sorted(valores)
final = []
cont = 0
for i in range(len(intervalos)):
    try:
        if valores[cont] <= intervalos[i]:
            cont += 1
            final.append(i + 1)
    except IndexError:
        continue
for i in range(len(final)):
        orden = valores.index(nueva[i])
        print(final[orden])

