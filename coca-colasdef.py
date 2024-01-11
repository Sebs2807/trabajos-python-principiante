lista = []
while True:
    inputs = input()
    if inputs:
        lista.append(inputs)
    else:
        break
for i in range(len(lista)):
    lista[i] = int(lista[i])
    if lista[i] >= 1 and lista[i] <= 200:
        bllenas = lista[i]
        bvacias = lista[i]
        consumidas = bllenas
        if bvacias == 2:
            bvacias += 1
        while bvacias >= 3:
            cambiadas = bvacias // 3
            bvacias = cambiadas + (bvacias - (cambiadas * 3))
            if bvacias == 2:
                bvacias = bvacias + 1
            consumidas = consumidas + cambiadas
    print(consumidas)


