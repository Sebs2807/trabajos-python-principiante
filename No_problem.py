cont = 1
while True:
    n = int(input())
    if n < 0:
        break
    hechos = input().split(" ")
    for i in range(len(hechos)):
        hechos[i] = int(hechos[i])
    necesarios = input().split(" ")
    for i in range(len(necesarios)):
        necesarios[i] = int(necesarios[i])
    print("Case " + str(cont) + ":")
    for i in range(12):
        if necesarios[i] <= n:
            print("No problem! :D")
            n = n - necesarios[i]
        else:
            print("No problem. :(")
        n = n + hechos[i]
    cont = cont + 1

    