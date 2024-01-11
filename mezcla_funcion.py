def mezclador(lista1,lista2):
    """Mezcla 2 listas ya organizadas y retorna una lista organizada de las 2
    (list) -> list
    """
    n1 = len(lista1)
    n2 = len(lista2)
    ordenada = []
    l1 = 0
    l2 = 0
    while l1 < n1 and l2 < n2:
        if lista1[l1] < lista2[l2]:
            ordenada.append(lista1[l1])
            l1 += 1
        else:
            ordenada.append(lista2[l2])
            l2 += 1
    if l1 < n1:
        ordenada + lista1[l1:]
    if l2 < n2:
        ordenada + lista2[l2:]
    
    return ordenada
mezclador([2,3,4,5,11,13],[3,6,9,12])
