lista = []

while True:
    m, n = map(int, input().split())
    if m == 0 or n == 0:
        break
    lista.append((m, n))

for i in range(len(lista)):
    if lista[i][0] > 0 and lista[i][1] > 0:
        print("primeiro")
    elif lista[i][0] < 0 and lista[i][1] > 0:
        print("segundo")
    elif lista[i][0] < 0 and lista[i][1] < 0:
        print("terceiro")
    else:
        print("quarto")
