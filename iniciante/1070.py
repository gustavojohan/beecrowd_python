valor = int(input())

for i in range(6):
    if valor % 2 == 0:
        valor += 1
        
    print(valor)
    valor += 2
