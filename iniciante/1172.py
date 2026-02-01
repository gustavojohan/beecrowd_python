vetor = []

for i in range(10):
    valor = int(input())
    vetor.append(valor if valor > 0 else 1)

    print(f"X[{i}] = {vetor[i]}")
