lista = []
cont = 0

for i in range(5):
    lista.append(float(input()))

for numero in lista:
    if numero % 2 == 0:
        cont += 1


print(f"{cont} valores pares")
