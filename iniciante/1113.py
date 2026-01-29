lista = []

while True:
    m, n = map(int, input().split())
    if m == n:
        break
    lista.append((m, n))

for i in range(len(lista)):
    print("Crescente") if lista[i][0] < lista[i][1] else print("Decrescente")
