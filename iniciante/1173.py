vetor = []

valor = int(input())
vetor.append(valor)

for i in range(0, 10):
    vetor.append(vetor[i]*2)
    print(f"N[{i}] = {vetor[i]}")