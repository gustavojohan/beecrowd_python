n = int(input())
inicio = 1

for i in range(n):
    for j in range(1, 4):
        if j != 3:
            print(inicio ** j, end=" ")
        else:
            print(inicio ** j, end="")
    print()
    inicio += 1