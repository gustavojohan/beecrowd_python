lista = []

while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    lista.append((m, n))

for i in range(len(lista)):
    soma = 0
    for j in range(lista[i][0], lista[i][1]+1) if lista[i][0] < lista[i][1] else range(lista[i][1], lista[i][0]+1):
        print(j, end=' ')
        soma += j
    print(f"Sum={soma}")
