lista = []
cont = 0

for i in range(6):
    lista.append(float(input()))

for numero in lista:
    if numero > 0:
        cont += 1

print(f"{cont} valores positivos")