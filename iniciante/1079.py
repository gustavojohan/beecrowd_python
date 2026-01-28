x = int(input())
lista = []

for i in range(x):
    lista.append(list(map(float, input().split())))

pesos = [2, 3 ,5]

for i in range(x):
    soma = 0
    for j in range(3):
        soma += lista[i][j] * pesos[j]
    print(f"{soma/sum(pesos):.1f}")
