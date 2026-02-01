lista = []
lista.append(float(input()))

for i in range(100):
    print(f"N[{i}] = {lista[(i)]:.4f}")
    lista.append(lista[i]/2)