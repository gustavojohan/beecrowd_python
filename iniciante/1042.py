v1, v2, v3 = map(int, input().split())

if v1 < v2 and v1 < v3:
    print(v1)
    if v2 < v3:
        print(v2)
        print(v3)
    else:
        print(v3)
        print(v2)
elif v2 < v1 and v2 < v3:
    print(v2)
    if v3 < v1:
        print(v3)
        print(v1)
    else:
        print(v1)
        print(v3)
elif v3 < v1 and v3 < v2:
    print(v3)
    if v1 < v2:
        print(v1)
        print(v2)
    else:
        print(v2)
        print(v1)

print('')

print(v1, v2, v3, sep='\n')