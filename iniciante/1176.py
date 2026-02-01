t = int(input())

for i in range(t):
    indice = int(input())
    lista = []

    for i in range(indice+1):
        if i == 0:
            lista.append(0)
        elif i == 1:
            lista.append(1)
        else:
            lista.append(lista[i-1] + lista[i-2])

    print(f"Fib({indice}) = {lista[i]}")