t = int(input())

for i in range(t):
    pa, pb, g1, g2 = input().split()

    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)

    cont = 0

    while True:
        if pa > pb or cont > 100:
            break
        
        pa += (pa * g1)//100
        pb += (pb * g2)//100
        cont += 1

    print(f"{cont} anos." if cont <= 100 else f"Mais de 1 seculo.")