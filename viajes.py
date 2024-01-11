final = []
while True:
    linea1 = input().split(" ")
    cantidadv = int(linea1[0])
    cantidadc = int(linea1[1])
    if cantidadc == 0 and cantidadv == 0:
        break
    linea2 = input()
    compvuelo = linea2.split(" ")
    compvuelo[0] = int(compvuelo[0])
    for i in range(1,len(compvuelo)):
        compvuelo[i] = int(compvuelo[i - 1]) + int(compvuelo[i])
    for i in range(len(compvuelo)):
        if cantidadc < compvuelo[i]:
            final.append(i)
            break
        if cantidadc <= compvuelo[i]:
            final.append(i + 1)
            break
        if cantidadc > compvuelo[-1]:
            final.append(cantidadv)
for i in range (len(final)):
    print(final[i])