soma = 1

for i in range(1, 20):
    soma += ((i*2)+1) / (2**i)

print(f"{soma:.2f}")