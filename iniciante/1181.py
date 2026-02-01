l = int(input())
T = input().upper()

matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

if T == 'S':
    print(sum(matriz[l]))
elif T == 'M':
    print(sum(matriz[l])/len(matriz[l]))