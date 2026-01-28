lista = []
cont = 0
soma = 0

for i in range(6):
    lista.append(float(input()))

for numero in lista:
    if numero > 0:
        cont += 1
        soma += numero

print(f"{cont} valores positivos")
print(f"{(soma/cont):.1f}")