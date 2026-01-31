n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    soma = x
    lista = []
    for i in range(y):
        if x%2 != 0:
            lista.append(soma)
            soma += 2
            
        else:
            x += 1
            soma = x
            lista.append(soma)
            soma += 2
            
    print(sum(lista))