n = int(input())
x = list(map(int, input().split()))

x = x[:n]

indice, menor = min(enumerate(x), key=lambda t: t[1])

print(f"Menor valor: {menor}")
print(f"Posicao: {indice}")
