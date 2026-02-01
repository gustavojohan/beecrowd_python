t = int(input())

for i in range(t):
    x = int(input())
    qnt_divisores = 0
    eh_primo = True

    for j in range(1, x+1):
        if x % j == 0:
            qnt_divisores += 1
        if qnt_divisores > 2:
            eh_primo = False
            break
    if not eh_primo:
        print(f"{x} nao eh primo")
    else:
        print(f"{x} eh primo")