n = int(input())
lista = []

for i in range(n):
    lista.append(tuple(map(int, input().split())))

for i in range(len(lista)):
    soma = 0
    for j in range(lista[i][0]+1, lista[i][1]) if lista[i][0] < lista[i][1] else range(lista[i][1]+1, lista[i][0]):
        if j % 2 != 0:
            soma += j
    print(soma)