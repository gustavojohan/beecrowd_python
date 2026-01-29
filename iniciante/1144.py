n = int(input())
inicio = 1

for i in range(n):
    for j in range(1, 4):
        if j != 3:
            print(inicio ** j, end=" ")
        else:
            print(inicio ** j, end="")
    print()
    print(inicio, end=' ')
    for j in range(2, 4):
        if j != 3:
            print(inicio ** j + 1, end=" ")
        else:
            print(inicio ** j + 1, end="")
    print()
    inicio += 1