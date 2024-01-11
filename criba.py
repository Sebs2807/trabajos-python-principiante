def main():
    n = int(input("Ingrese el número hasta el que desea saber la cantidad de números primos"))
    criba = []
    for i in range(0,n + 1):
        criba.append(True)
    x = len(criba)
    for i in range(2,x):
        if criba[i]:
            for j in range(i * 2,x,i):
                criba[j] = False
    contar = criba[2:x-1]
    print(contar)
    cantidad = contar.count(True)
    if criba[x - 1]:
        print(n,"es primo")
        print("Hay",cantidad,"primos menores que",n)
    else:
        print(n,"no es primo")
        print("Hay",cantidad,"primos menores que",n)
main()