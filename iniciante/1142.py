n = int(input())
inicio = 1

for i in range(n):
    for j in range(3):
        print(inicio, end=' ')
        if j != 2:
            inicio += 1
    print("PUM")
    inicio += 2