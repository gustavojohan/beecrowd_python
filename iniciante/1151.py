n = int(input())
lista = []

for i in range(n):
    if i == 0:
        lista.append(0)
    elif i == 1:
        lista.append(1)
    else:
        lista.append(lista[i-1] + lista[i-2])

print(*lista)