t = int(input())
cont = 0

for i in range(1000):
    if cont < t:
        print(f"N[{i}] = {cont}")
        cont += 1
    else:
        cont = 0
        print(f"N[{i}] = {cont}")
        cont += 1