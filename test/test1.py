"""
Este test consiste en probar un programa que obtenga los indices
de los elementos repetidos de una lista.
"""

lista = [1,1,2,2,3,4,1,5,3,2,1,1,3]
unico = []
num_an = []
rep = {}

for elem in lista:
    if elem not in unico:
        unico.append(elem)
    else:
        if elem not in rep.values():
            rep[elem] = [lista.index(elem)]

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if (lista[i] == lista[j]) and (i not in num_an):
            rep[lista[i]].append(j)
            num_an.append(i)

print(rep.keys())
