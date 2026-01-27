code, amount = map(int, input().split())

if code == 1:
    print(f'Total: R$ {float(4*amount):.2f}')
elif code == 2:
    print(f'Total: R$ {float(4.50*amount):.2f}')
elif code == 3:
    print(f'Total: R$ {float(5*amount):.2f}')
elif code == 4:
    print(f'Total: R$ {float(2*amount):.2f}')
elif code == 5:
    print(f'Total: R$ {float(1.50*amount):.2f}')