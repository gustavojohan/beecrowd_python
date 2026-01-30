lista = list(map(int, input().split()))
a, n = [valor for valor in lista if valor > 0]

soma = 0

for i in range(n):
    soma += a + i

print(soma)