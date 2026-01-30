x = int(input())
soma = 0
cont = 0

while (z := int(input())) <= x:
    continue

for i in range(x, z+1):
    soma += i
    cont += 1
    if soma >= z:
        break

print(cont)