x = int(input())
lista_valores = []

for i in range(x):
    lista_valores.append(int(input()))

for valor in lista_valores:
    if valor > 0:
        if valor % 2 == 0:
            print("EVEN POSITIVE")
        elif valor % 2 != 0:
            print("ODD POSITIVE")
    elif valor < 0:
        if valor % 2 == 0:
            print("EVEN NEGATIVE")
        elif valor % 2 != 0:
            print("ODD NEGATIVE")
    else:
        print("NULL")